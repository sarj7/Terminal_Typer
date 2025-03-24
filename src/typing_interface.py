import sys
import os
import time
import termios
import tty
import shutil
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
        # Get terminal size
        self.terminal_width, self.terminal_height = shutil.get_terminal_size()
        # Calculate how many lines of text we can display (accounting for UI elements)
        self.max_display_lines = self.terminal_height - 10  # Reserve space for UI elements
        self.scroll_position = 0  # Track which part of text is visible

    def getch(self):
        """Get a single character from user input with improved escape sequence handling"""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            
            # Read first character
            ch = sys.stdin.read(1)
            
            # If it's ESC, check if it's part of an escape sequence (like arrow keys)
            if ch == '\x1b':  # ESC character
                # Brief timeout to check for more characters
                import select
                if select.select([sys.stdin], [], [], 0.1)[0]:  # More characters available
                    # It's an escape sequence (like arrow keys), read and ignore the rest
                    while select.select([sys.stdin], [], [], 0.1)[0]:
                        sys.stdin.read(1)  # Consume the rest of the sequence
                    return '\x00'  # Return a harmless character
                else:
                    # It's a genuine ESC key press
                    return ch
            else:
                return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def display_text(self):
        """Reset and simplify the display approach"""
        # Clear the screen
        os.system('clear')
        
        # Get current cursor position
        cursor_pos = len(self.user_input)
        
        # Simplify by directly using the text without complex formatting
        display_width = self.terminal_width - 5
        
        # Convert text to lines for display (simple wrapping)
        text_lines = []
        current_line = ""
        line_indices = []  # Starting index of each line
        current_indices = []
        
        for i, char in enumerate(self.text):
            current_line += char
            current_indices.append(i)
            
            if len(current_line) >= display_width or char == '\n':
                text_lines.append(current_line.rstrip('\n'))
                line_indices.append(current_indices[0])  # Start index of this line
                current_line = ""
                current_indices = []
        
        # Add the last line if needed
        if current_line:
            text_lines.append(current_line)
            line_indices.append(current_indices[0])
        
        # Find line with cursor
        current_line_index = 0
        for i, start_idx in enumerate(line_indices):
            next_idx = line_indices[i+1] if i+1 < len(line_indices) else len(self.text)
            if start_idx <= cursor_pos < next_idx:
                current_line_index = i
                break
        
        # Always show at least first 6 lines to ensure beginning is visible
        visible_start = 0 if current_line_index < 6 else current_line_index - 5
        visible_end = min(len(text_lines), visible_start + self.max_display_lines)
        
        # Display header
        print("Terminal Typer - Type the text below:")
        print("-" * display_width)
        
        # Display each line with color highlighting
        for i in range(visible_start, visible_end):
            line = text_lines[i]
            start_idx = line_indices[i]
            
            # Format this line with color highlighting
            formatted_line = ""
            for j, char in enumerate(line):
                char_idx = start_idx + j
                
                if char_idx < cursor_pos:
                    # Already typed characters
                    if char_idx < len(self.user_input) and self.user_input[char_idx] == char:
                        formatted_line += f"\033[32m{char}\033[0m"  # Green for correct
                    else:
                        formatted_line += f"\033[31m{char}\033[0m"  # Red for wrong
                elif char_idx == cursor_pos:
                    # Current cursor position
                    formatted_line += f"\033[4m{char}\033[0m"  # Underlined
                else:
                    # Not yet typed
                    formatted_line += char
            
            print(formatted_line)
        
        # Show indicators and progress
        print("-" * display_width)
        if visible_start > 0:
            print("↑ More text above")
        if visible_end < len(text_lines):
            print("↓ More text below")
            
        progress = min(100, int((len(self.user_input) / len(self.text)) * 100))
        print(f"Progress: {progress}% | Press ESC to finish | Typed: {len(self.user_input)}/{len(self.text)}")
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
                if char == '\x1b':  # ESC key
                    break
                    
                # Ignore special character we use to represent consumed escape sequences
                elif char == '\x00':
                    continue
                    
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