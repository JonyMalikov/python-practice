"""217. Contains Duplicate.

https://leetcode.com/problems/contains-duplicate/

Дан массив целых чисел nums.
Верни True, если хотя бы одно число встречается дважды, иначе False.
"""


def contains_duplicate(nums: list[int]) -> bool:
    """Решение 1: через set. Схлопываем дубликаты и сравниваем длины.

    Time:  O(n)
    Space: O(n)
    """
    return len(nums) != len(set(nums))


def contains_duplicate_early_exit(nums: list[int]) -> bool:
    """Решение 2: цикл с ранним выходом.

    Останавливаемся на первом найденном дубликате.

    Time:  O(n) worst, O(1) best
    Space: O(n)
    """
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    # Базовые случаи
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False

    # Edge cases
    assert contains_duplicate([]) is False            # пустой массив
    assert contains_duplicate([5]) is False           # один элемент
    assert contains_duplicate([7, 7]) is True         # два одинаковых
    assert contains_duplicate([3, 3, 3]) is True      # все одинаковые
    assert contains_duplicate([-1, -2, -1]) is True   # отрицательные

    # Проверка второй версии на тех же случаях
    assert contains_duplicate_early_exit([1, 2, 3, 1]) is True
    assert contains_duplicate_early_exit([1, 2, 3, 4]) is False
    assert contains_duplicate_early_exit([]) is False
    assert contains_duplicate_early_exit([5]) is False
    assert contains_duplicate_early_exit([7, 7]) is True
    assert contains_duplicate_early_exit([-1, -2, -1]) is True

    print("All tests passed ✅")  # noqa: T201