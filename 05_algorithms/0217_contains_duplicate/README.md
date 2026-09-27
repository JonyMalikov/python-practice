# 217. Contains Duplicate

**Источник:** [LeetCode](https://leetcode.com/problems/contains-duplicate/)
**Тема:** Arrays & Hashing
**Сложность:** Easy
**Дата:** 25.09.2026

## Идея

`set` схлопывает дубликаты — если длина уменьшилась, значит были повторы.

## Решения

### 1. Через `set` (основное)
```python
return len(nums) != len(set(nums))