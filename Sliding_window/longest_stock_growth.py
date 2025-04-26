"""
Рост акций компании

средне
решено

Дан массив stock, где stock[i] = 1 означает рост акций в i-й день, а stock[i] = -1 — падение.
Требуется найти максимальное количество подряд идущих дней роста акций.

Нумерация в массиве начинается с единицы, а не с нуля.

Пример 1:

Ввод: stock = [-1,1,-1,1,1,1,1,-1,1]
Вывод: 4
Объяснение: Самый долгий рост акций - 4 дня (с 4 по 7 день).

Пример 2:

Ввод: stock = [1,-1,-1,1]
Вывод: 1

Ограничения:

0 <= len(stock)
Значение массива stock это -1 или 1
"""

from typing import *


def longest_stock_growth(stock: List[int]) -> int:
    l = 0
    r = 0
    result = 0
    while l < len(stock):
        while r + 1 < len(stock) and stock[r] == stock[r + 1]:
            r += 1

        if stock[r] == 1:
            result = max(result, r - l + 1)

        l = r + 1
        r = r + 1
    return result

if __name__ == "__main__":
    ex1 = [-1,1,-1,1,1,1,1,-1,1]
    ex2 = [1,-1,-1,1]

    ans1 = longest_stock_growth(ex1)
    ans2 = longest_stock_growth(ex2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - длина массива stock
Память: O(1)
"""