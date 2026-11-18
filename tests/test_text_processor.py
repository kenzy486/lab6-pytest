import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.text_processor import TextProcessor

pytestmark = pytest.mark.text


@pytest.fixture
def tp():
    """A TextProcessor for each test."""
    return TextProcessor()


# ----------------------------------------------------------------- reverse

@pytest.mark.parametrize("text, expected", [
    ("a", "a"),
    ("", ""),
    pytest.param("hello", "olleh", marks=pytest.mark.xfail(reason="BUG #5: reverse returns the original string instead of reversing it", strict=True)),
    pytest.param("ab", "ba", marks=pytest.mark.xfail(reason="BUG #5: reverse returns the original string instead of reversing it", strict=True)),
])
def test_reverse(tp, text, expected):
    assert tp.reverse(text) == expected


# ------------------------------------------------------------ count_vowels

@pytest.mark.parametrize("text, expected", [
    ("hello", 2),
    ("xyz", 0),
    ("", 0),
    pytest.param("AEIOU", 5, marks=pytest.mark.xfail(reason="BUG #6: count_vowels does not count uppercase vowels", strict=True)),
    pytest.param("HeLLo WoRLD", 2, marks=pytest.mark.xfail(reason="BUG #6: count_vowels does not count uppercase vowels", strict=True)),
])
def test_count_vowels(tp, text, expected):
    assert tp.count_vowels(text) == expected


# ----------------------------------------------------------- is_palindrome

@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    pytest.param("nurses run", True, marks=pytest.mark.xfail(reason="BUG #7: is_palindrome does not ignore spaces", strict=True)),
    pytest.param("RaceCar", True, marks=pytest.mark.xfail(reason="BUG #7: is_palindrome does not ignore letter case", strict=True)),
])
def test_is_palindrome(tp, text, expected):
    assert tp.is_palindrome(text) is expected


# -------------------------------------------------------------- word_count

@pytest.mark.parametrize("text, expected", [
    ("hello world", 2),
    pytest.param("hello   world", 2, marks=pytest.mark.xfail(reason="BUG #8: word_count counts empty strings between repeated spaces", strict=True)),
    pytest.param("  hello world  ", 2, marks=pytest.mark.xfail(reason="BUG #8: word_count counts empty strings caused by leading and trailing spaces", strict=True)),
])
@pytest.mark.edge
def test_word_count(tp, text, expected):
    assert tp.word_count(text) == expected


# -------------------------------------------------------- capitalize_words

@pytest.mark.parametrize("text, expected", [
    ("hello world", "Hello World"),
    ("PYTHON", "Python"),
    ("", ""),
])
def test_capitalize_words(tp, text, expected):
    assert tp.capitalize_words(text) == expected


# ---------------------------------------------------------------- truncate

@pytest.mark.parametrize("text, max_length, expected", [
    ("Hello World", 5, "Hello..."),
    pytest.param("Hi", 5, "Hi", marks=pytest.mark.xfail(reason="BUG #9: truncate appends ellipsis even when the text is shorter than max_length", strict=True)),
    pytest.param("Hello", 5, "Hello", marks=pytest.mark.xfail(reason="BUG #9: truncate appends ellipsis when text length equals max_length", strict=True)),
])
@pytest.mark.edge
def test_truncate(tp, text, max_length, expected):
    assert tp.truncate(text, max_length) == expected
