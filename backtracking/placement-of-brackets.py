"""
Расстановка скобок

средне
решено

Дано число n, обозначающее количество пар круглых скобок.
Напишите функцию, которая генерирует все уникальные комбинации корректно составленных
скобочных последовательностей из n пар.

Пример 1:

Ввод: n = 2
Вывод: ["(())","()()"]

Пример 2:

Ввод: n = 1
Вывод: ["()"]

Ограничения:

n >= 1
"""

from typing import *


def generate_brackets(n: int) -> List[str]:
    res = []

    def generage(prefix: str, opened: int, closed: int):
        if len(prefix) == 2 * n:
            res.append(prefix)
            return

        if opened < n:
            generage(prefix + '(', opened + 1, closed)

        if closed < opened:
            generage(prefix + ')', opened, closed + 1)

    generage("", 0, 0)
    return res

if __name__ == "__main__":
    ex1 = 2
    ex2 = 1

    ans1 = generate_brackets(ex1)
    ans2 = generate_brackets(ex2)

    print(ans1)
    print(ans2)



"""
Оценка сложности

Время: O(n * 4n) или более точно O(n * Cn), где Cn - n-ое число Каталана
Память: O(n * 4n) или более точно O(n * Cn), где Cn - n-ое число Каталана
"""
