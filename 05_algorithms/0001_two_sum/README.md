# 1. Two Sum

**Источник:** [LeetCode](https://leetcode.com/problems/two-sum/)
**Тема:** Arrays & Hashing
**Сложность:** Easy
**Дата:** XX.XX.2026

## Идея

Для каждого `num` ищем **уже виденное** `target - num` в `dict`.
Если нашли — пара есть.

## Решение

Файл: `two_sum.py`

```python
seen: dict[int, int] = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i