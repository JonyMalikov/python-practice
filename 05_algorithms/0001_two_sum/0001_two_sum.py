"""1. Two Sum.

https://leetcode.com/problems/two-sum/

Дан массив целых чисел nums и число target.
Верни индексы двух чисел, дающих в сумме target.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Находит индексы двух чисел, дающих в сумме target.

    Time:  O(n)
    Space: O(n)
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # Базовые случаи
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Edge cases
    assert two_sum([3, 3], 6) == [0, 1]  # одинаковые числа
    assert two_sum([-1, -2, -3], -5) == [1, 2]  # отрицательные
    assert two_sum([0, 4, 0], 0) == [0, 2]  # ноль в массиве
    assert two_sum([1, 2], 3) == [0, 1]  # минимальный массив

    print("All tests passed ✅")
