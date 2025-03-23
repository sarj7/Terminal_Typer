import sys
import os
import time
import termios
import tty
from collections import Counter

class TypingInterface:
    def __init__(self, text):
        self.text = text
        self.user_input = ""
        self.errors = []
        self.correct_count = 0
        self.total_count = 0
        self.cursor_pos = 0
        self.start_time = None
        self.end_time = None
        self.metrics = None

    def getch(self):
        """Get a single character from user input"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def display_text(self):
        """Display text with real-time feedback"""
        print("\033[H\033[J", end="")  # Clear screen
        print("Type the following text:\n" + "-" * 80)
        
        # Display color-coded text based on user input
        for i, char in enumerate(self.text):
            if i < len(self.user_input):
                color = "\033[32m" if self.user_input[i] == char else "\033[31m"
                sys.stdout.write(f"{color}{char}\033[0m")
            elif i == len(self.user_input):
                sys.stdout.write(f"\033[4m{char}\033[0m")
            else:
                sys.stdout.write(char)
        
        print("\n" + "-" * 80)
        progress = min(100, int((len(self.user_input) / len(self.text)) * 100))
        print(f"Progress: {progress}% | Press ESC to finish")
        sys.stdout.flush()
    
    def start_typing_practice(self):
        """Main typing practice loop"""
        repeat_same_text = True
        
        while repeat_same_text:
            # Reset state for a new session
            self.user_input = ""
            self.errors = []
            self.correct_count = 0
            self.total_count = 0

            from metrics import Metrics
            self.metrics = Metrics()
            self.metrics.start_timer()
            
            self.display_text()
            
            while len(self.user_input) < len(self.text):
                char = self.getch()
                
                # ESC key to exit
                if ord(char) == 27:
                    break
                    
                # Backspace/Delete key
                elif ord(char) in (8, 127) and len(self.user_input) > 0:
                    self.user_input = self.user_input[:-1]
                    self.total_count -= 1
                    
                # Regular character input
                elif ord(char) >= 32:  # Printable characters
                    self.user_input += char
                    self.total_count += 1
                    
                    # Check if correct
                    idx = len(self.user_input) - 1
                    if idx < len(self.text):
                        if char == self.text[idx]:
                            self.correct_count += 1
                        else:
                            self.errors.append(char)
                
                self.display_text()
            
            self.metrics.stop_timer()
            self.metrics.update_metrics(self.user_input, self.text)
            
            # Print final statistics
            print("\nTyping session completed!")
            print("\n--- Performance Metrics ---")
            
            # Calculate and display metrics directly
            elapsed_time = self.metrics.end_time - self.metrics.start_time
            total_chars = len(self.text)
            typed_chars = len(self.user_input)
            correct_chars = sum(1 for i, c in enumerate(self.user_input) if i < len(self.text) and c == self.text[i])
            accuracy = (correct_chars / typed_chars * 100) if typed_chars > 0 else 0
            
            # Calculate WPM: (characters typed / 5) / minutes elapsed
            # Using the standard definition where 5 characters = 1 word
            minutes = elapsed_time / 60
            wpm = (typed_chars / 5) / minutes if minutes > 0 else 0
            
            # Show the calculated metrics
            print(f"Words Per Minute (WPM): {wpm:.2f}")
            print(f"Accuracy: {accuracy:.2f}%")
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            print(f"Characters Typed: {typed_chars}/{total_chars}")
            print(f"Correct Characters: {correct_chars}")
            print(f"Errors: {typed_chars - correct_chars}")
            
            # Display most common errors
            print("\nMost Common Errors:")
            error_counts = Counter(self.errors)
            for char, count in error_counts.most_common(5):  # Display top 5 errors
                print(f"  '{char}': {count} times")
            
            # Clear prompt about repeating
            print("\n" + "-" * 40)
            choice = input("Would you like to try the same text again? (y/n): ").strip().lower()
            if choice != 'y':
                new_text_choice = input("Would you like to practice with new text? (y/n): ").strip().lower()
                if new_text_choice == 'y':
                    # Return to main flow to get new text
                    return True
                else:
                    # Exit completely
                    return False
        
        return False  # Default return, should not be reached

    def calculate_metrics(self):
        """Calculate accuracy and errors"""
        accuracy = (self.correct_count / len(self.user_input)) * 100 if len(self.user_input) > 0 else 0
        return accuracy, self.errors

    def get_typing_data(self):
        """Return typing session data"""
        return {
            'typed_text': self.user_input,
            'reference_text': self.text
        }