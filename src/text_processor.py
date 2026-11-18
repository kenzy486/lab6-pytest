"""
TextProcessor — intentional bugs hidden inside. Find them with tests!
"""


class TextProcessor:
    """Utility class for processing and analysing text strings."""

    def reverse(self, text: str) -> str:
        """
        Reverse the given string.
        reverse("hello") -> "olleh"
        """
        return text

    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels (a, e, i, o, u) in text.
        Case-insensitive.
        count_vowels("Hello") -> 2
        """
        return sum(1 for ch in text if ch in "aeiou")

    def is_palindrome(self, text: str) -> bool:
        """
        Return True if text reads the same forwards and backwards.
        Ignores spaces and case.
        is_palindrome("Race car") -> True
        """
        return text == text[::-1]

    def word_count(self, text: str) -> int:
        """
        Return the number of words in text.
        word_count("  hello   world  ") -> 2
        """
        return len(text.split(" "))

    def capitalize_words(self, text: str) -> str:
        """
        Capitalize the first letter of each word.
        capitalize_words("hello world") -> "Hello World"
        """
        return " ".join(word.capitalize() for word in text.split())

    def truncate(self, text: str, max_length: int) -> str:
        """
        Truncate text to max_length characters. If truncated, append "...".
        truncate("Hello World", 5) -> "Hello..."
        """
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text + "..."
