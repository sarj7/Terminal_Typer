import re

class Metrics:
    def __init__(self):
        self.correct_words = 0
        self.errors = {}
        self.start_time = None
        self.end_time = None
        # For optional character-level accuracy:
        self.total_chars = 0
        self.correct_chars = 0
        # Store last texts used for metric calculation
        self.typed_text = None
        self.reference_text = None

    def start_timer(self):
        from time import time
        self.start_time = time()

    def stop_timer(self):
        from time import time
        self.end_time = time()

    def update_metrics(self, typed_text, reference_text):
        # Save texts so display_metrics can know update_metrics was used
        self.typed_text = typed_text
        self.reference_text = reference_text

        # Update character-level counts (optional)
        self.total_chars = len(typed_text)
        self.correct_chars = sum(1 for t, r in zip(typed_text, reference_text) if t == r)
        for t, r in zip(typed_text, reference_text):
            if t != r:
                self.errors[t] = self.errors.get(t, 0) + 1

        # Recalculate correct_words based solely on exact word matches.
        # A word is counted only if it exactly matches the corresponding reference word.
        typed_words = typed_text.split()
        reference_words = reference_text.split()
        self.correct_words = 0
        for i in range(min(len(typed_words), len(reference_words))):
            if typed_words[i] == reference_words[i]:
                self.correct_words += 1

    def calculate_speed(self):
        """
        Net WPM = (number of complete, correct words) / (elapsed minutes).
        Only words that exactly match the reference word are counted.
        """
        if self.start_time and self.end_time:
            elapsed_time = self.end_time - self.start_time
            if elapsed_time > 0:
                elapsed_minutes = elapsed_time / 60.0
                return self.correct_words / elapsed_minutes
        return 0.0

    def calculate_accuracy(self):
        if self.total_chars > 0:
            return (self.correct_chars / self.total_chars) * 100
        return 0.0

    def get_most_common_errors(self):
        sorted_errors = sorted(
            self.errors.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return sorted_errors[:10]

    def display_metrics(self):
        """
        Before displaying, it is assumed that update_metrics has been called
        so that the metrics reflect the latest typing session.
        """
        speed = self.calculate_speed()
        accuracy = self.calculate_accuracy()
        common_errors = self.get_most_common_errors()

        print("\n=== Typing Metrics ===")
        print(f"Typing Speed: {speed:.2f} WPM")
        print(f"Accuracy: {accuracy:.2f}% (character-level)")

        if common_errors:
            print("\nMost Common Errors:")
            for char, count in common_errors:
                print(f"  '{char}': {count} times")
        else:
            print("\nNo errors! Perfect typing!")