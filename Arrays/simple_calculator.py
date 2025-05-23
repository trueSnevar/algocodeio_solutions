"""
Простой калькулятор

средне
решено

Дан массив s с положительными числами и знаками * и +.
Нужно вернуть результат вычислений и важно, чтобы решение было за O(1) по дополнительной памяти.

Пример 1:

Ввод: s = ["2","*","3","*","1","+","2","+","2","+","2","*","0","*","13","+","1"]
Вывод: 11

Порядок операций:

2*3*1 = 6

6 + 2 + 2 = 10

2*0*13 = 0 → 10 + 0 = 10

10 + 1 = 11

Пример 2:

Ввод: s = ["1","+","2","+","3"]
Вывод: 6

Ограничения:

len(s) >= 1

"""

from typing import *

def calculate(s: List[str]) -> int:
    result = 0
    # prev_multiply - произведение подряд идущих чисел
    prev_multiply = int(s[0])
    i = 0
    # итерируемся по знакам
    for i in range(1, len(s), 2):
        if s[i] == "*":
            # при умножении домножаем следующее число на накопленное произведение
            prev_multiply *= int(s[i + 1])
        elif s[i] == "+":
            # когда встречаем знак "+" обновляем prev_multiply и прибавляем
            #  текущее произведение подряд идущих чисел в результат
            result += prev_multiply
            prev_multiply = int(s[i + 1])
    result += prev_multiply
    return result


if __name__ == "__main__":
    ex1 = ["2","*","3","*","1","+","2","+","2","+","2","*","0","*","13","+","1"] # 11
    ex2 = ["1","+","2","+","3"] # 6

    ans1 = calculate(ex1)
    ans2 = calculate(ex2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - длина массива nums
Память: O(1)
"""