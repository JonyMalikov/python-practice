from collections import defaultdict


class Solution:
    """LeetCode 0049. Группировка анаграмм.

    Группирует строки по сигнатуре частот символов.
    Время: O(N * K), где N — количество строк, K — максимальная длина строки.
    Память: O(N * K) для хеш-таблицы и результата.
    """

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """Группирует анаграммы, используя кортеж из 26 частот в качестве ключа."""
        groups: defaultdict[tuple[int, ...], list[str]] = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())
