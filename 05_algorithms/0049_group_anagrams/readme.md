# 0049. Group Anagrams

**Источник:** [LeetCode](https://leetcode.com/problems/group-anagrams/)
**Тема:** Arrays & Hashing
**Сложность:** Medium
**Дата:** 24.09.2026

## Идея

Анаграммы при сортировке букв дают одинаковую строку (сигнатуру). 
Используем отсортированную строку как ключ в хеш-таблице (`defaultdict`), чтобы собрать все исходные слова в группы.

Альтернативный (более быстрый) подход — использовать кортеж из 26 частот символов в качестве ключа.

## Решения

### 1. Через сортировку (основное, O(N * K log K))
```python
from collections import defaultdict
from typing import List

class Solution:
    """LeetCode 0049. Group Anagrams.

    Groups strings by their sorted character signature.
    Time: O(N * K log K), where N is number of strings, K is max length.
    Space: O(N * K) for the hashmap and output.
    """

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """Group anagrams together using a sorted string as a key."""
        groups: defaultdict[str, List[str]] = defaultdict(list)

        for s in strs:
            # Сортируем буквы слова, чтобы получить общую сигнатуру для анаграмм
            signature = ''.join(sorted(s))
            groups[signature].append(s)

        return list(groups.values())