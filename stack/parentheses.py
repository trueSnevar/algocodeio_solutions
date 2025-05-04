"""
Круглые скобки

легко
решено

Дана строка s, состоящая только из символов '(' и ')'.
Нужно вернуть true, если скобки в строке сбалансированы, иначе вернуть false.
Сбалансированная строка означает, что каждой открывающей скобке соответствует закрывающая,
и они правильно вложены друг в друга.

Пример 1:

Ввод: s = "()"
Вывод: true

Пример 2:

Ввод: s = "(()()"
Вывод: false

Пример 2:

Ввод: s = "))(("
Вывод: false

Ограничения:

len(s) >= 1
"""

from typing import *

def is_balanced(s: str) -> bool:
    balance = 0
    for brace in s:
        if brace == "(":
            balance += 1
        elif brace == ")":
            balance -= 1
        # Если balance < 0, значит закрывающих скобок больше, чем открывающих
        if balance < 0:
            return False
    return balance == 0

if __name__ == "__main__":
    ex1 = "()"
    ex2 = "(()()"
    ex3 = "))(("

    ans1 = is_balanced(ex1)
    ans2 = is_balanced(ex2)
    ans3 = is_balanced(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n), где n - размер строки s
Память: O(1)
"""

