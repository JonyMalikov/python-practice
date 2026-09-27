"""242. Valid Anagram.

https://leetcode.com/problems/valid-anagram/

Даны две строки s и t.
Верни True, если t — анаграмма s, иначе False.
"""

from collections import Counter


def is_anagram_sort(s: str, t: str) -> bool:
    """Решение 1: сортировка обеих строк.

    Time:  O(n log n)
    Space: O(n)
    """
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def is_anagram_counter(s: str, t: str) -> bool:
    """Решение 2: подсчёт частот через Counter.

    Time:  O(n)
    Space: O(k), где k — число уникальных символов
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    # Базовые случаи
    assert is_anagram_sort("anagram", "nagaram") is True
    assert is_anagram_sort("rat", "car") is False

    # Edge cases
    assert is_anagram_sort("", "") is True
    assert is_anagram_sort("", "a") is False
    assert is_anagram_sort("a", "a") is True
    assert is_anagram_sort("aab", "abb") is False
    assert is_anagram_sort("aa", "aa") is True

    # Проверка второй версии
    assert is_anagram_counter("anagram", "nagaram") is True
    assert is_anagram_counter("rat", "car") is False
    assert is_anagram_counter("", "") is True
    assert is_anagram_counter("", "a") is False
    assert is_anagram_counter("aab", "abb") is False

    print("All tests passed ✅")
