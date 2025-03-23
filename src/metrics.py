import time

class Metrics:
    def __init__(self):
        self.correct_words = 0
        self.errors = {}
        self.start_time = None
        self.end_time = None
        self.total_chars = 0
        self.correct_chars = 0
        self.typed_text = None
        self.reference_text = None

    def start_timer(self):
        """Start timing the session"""
        self.start_time = time.time()

    def stop_timer(self):
        """Stop timing the session"""
        self.end_time = time.time()

    def update_metrics(self, typed_text, reference_text):
        """Update typing metrics based on input"""
        self.typed_text = typed_text
        self.reference_text = reference_text
        
        # Update character-level stats
        self.total_chars = len(typed_text)
        self.correct_chars = sum(1 for t, r in zip(typed_text, reference_text) if t == r)
        
        # Track errors
        for t, r in zip(typed_text, reference_text):
            if t != r:
                self.errors[t] = self.errors.get(t, 0) + 1
        
        # Count correct words
        typed_words = typed_text.split()
        reference_words = reference_text.split()
        self.correct_words = sum(1 for t, r in zip(typed_words, reference_words) if t == r)

    def calculate_speed(self):
        """Calculate WPM"""
        if self.start_time and self.end_time:
            elapsed_minutes = (self.end_time - self.start_time) / 60.0
            return self.correct_words / elapsed_minutes if elapsed_minutes > 0 else 0
        return 0.0

    def calculate_accuracy(self):
        """Calculate typing accuracy percentage"""
        return (self.correct_chars / self.total_chars * 100) if self.total_chars > 0 else 0.0

    def get_most_common_errors(self, limit=10):
        """Get most frequent typing errors"""
        return sorted(self.errors.items(), key=lambda x: x[1], reverse=True)[:limit]