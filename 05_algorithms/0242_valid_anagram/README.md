# 242. Valid Anagram

**Источник:** [LeetCode](https://leetcode.com/problems/valid-anagram/)
**Тема:** Arrays & Hashing
**Сложность:** Easy
**Дата:** XX.XX.2026

## Идея

Анаграмма = одинаковые буквы в одинаковом количестве.
Достаточно сравнить частотные таблицы или отсортированные строки.

## Решения

### 1. Сортировка
```python
return sorted(s) == sorted(t)