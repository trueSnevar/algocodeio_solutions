"""
Хитрое сравнение строк

сложно
решено

Даны строки s и t. Нужно вернуть True, если после эмуляции ввода в текстовый редактор
(символ '#' означает удаление предыдущего символа) они окажутся одинаковыми.
Если перед '#' нет символа — ничего не удаляется.

Пример 1:

Ввод: s = "ac#b#ac", t = "abc##aa#b#c"
Вывод: True
Объяснение: после эмуляции обе строки становятся "aac".

Пример 2:

Ввод: s = "a#####b", t = "b"
Вывод: True
Объяснение: строки редактируются до "b".

Пример 3:

Ввод: s = "abcd", t = "abcd#"
Вывод: False
Объяснение: первая остаётся "abcd", вторая — "abc".

Ограничения:
- len(s), len(t) ≥ 0
"""
from typing import *

def backspace_compare(s: str, t: str) -> bool:
    """
    Сравнивает s и t после обработки символов '#'.
    Используется метод двух указателей с O(1) дополнительной памяти.
    """
    p1 = len(s) - 1
    p2 = len(t) - 1

    skip1 = 0
    skip2 = 0

    while p1 >= 0 or p2 >= 0:
        while p1 >= 0:
            if s[p1] == "#":
                skip1 += 1
                p1 -= 1
            elif skip1 > 0:
                p1 -= 1
                skip1 -= 1
            else:
                break

        while p2 >= 0:

            if t[p2] == "#":
                skip2 += 1
                p2 -= 1
            elif skip2 > 0:
                p2 -= 1
                skip2 -= 1
            else:
                break

        if p1 >= 0 and p2 >= 0 and s[p1] != t[p2]:
            return False

        if (p1 >= 0) != (p2 >= 0):
            return False

        p1 -= 1
        p2 -= 1

    return True


if __name__ == "__main__":
    # Пример 1
    print(backspace_compare("ac#b#ac", "abc##aa#b#c"))  # True
    # Пример 2
    print(backspace_compare("a#####b", "b"))            # True
    # Пример 3
    print(backspace_compare("abcd", "abcd#"))          # False

# Оценка сложности:
# Время: O(n + m), где n = len(s), m = len(t)
# Память: O(1) дополнительной памяти
