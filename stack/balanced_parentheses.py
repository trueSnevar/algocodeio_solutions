"""
Сбалансированные скобки

легко
решено

Дана строка s, содержащая символы (, ), {, }, [, ] и символы латинского алфавита.
Нужно определить, является ли строка s правильной.

Строка считается правильной, если:

Каждая открытая скобка имеет соответствующую закрывающую скобку того же типа.
Скобки закрываются в правильном порядке.
Символы латинского алфавита не влияют на правильность строки.

Пример 1:

Ввод: s = "Algo[[(C)od]]{e}the({Best}{[Pla]t}f)orm"
Вывод: true

Пример 2:

Ввод: s = "[]()))"
Вывод: false

Пример 3:

Ввод: s = "((()"
Вывод: false

Ограничения:

len(s) >= 1
"""

from typing import *

def is_balanced(s: str) -> bool:
    bm = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        # если скобка открытая - просто добавляем в стек
        if char in ('(', '[', '{'):
            stack.append(char)
        # перед нами закрывающаяся скобка
        elif char in bm:
            # если стек пуст, или на вершине не открывающая скобка такого же типа
            if not stack or stack[-1] != bm[char]:
                return False
            else:
                stack.pop()

    return len(stack) == 0

if __name__ == "__main__":
    ex1 = "Algo[[(C)od]]{e}the({Best}{[Pla]t}f)orm"
    ex2 = "[]()))"
    ex3 = "((()"

    ans1 = is_balanced(ex1)
    ans2 = is_balanced(ex2)
    ans3 = is_balanced(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n), где n - размер строки s
Память: O(n), где n - размер строки s
"""

