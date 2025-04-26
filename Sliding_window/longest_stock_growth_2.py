"""
Подставной отчет

средне
решено

Дан массив stock, где stock[i] = 1 означает рост акций в i-й день, а stock[i] = 0 — падение.

Компания терпит убытки и готовит отчет для инвесторов, в котором можно улучшить показатели,
заменив один день падения (0) на рост (1).

Требуется найти максимальное количество подряд идущих дней роста акций с учетом такой замены.

Нумерация в массиве начинается с единицы, а не с нуля.

Пример 1:

Ввод: stock = [1,1,0,1,1,1,1,0,1]
Вывод: 7
Объяснение: самый долгий рост акций с 1 по 7 день с заменой в 3 дне.

Пример 2:

Ввод: stock = [0]
Вывод: 1

Пример 3:

Ввод: stock = [1,0,0,1]
Вывод: 2

Ограничения:

0 <= len(stock)
Значение массива stock : 0 или 1
"""

from typing import *


def longest_stock_growth(stock: List[int]) -> int:
    l = 0
    r = -1
    zero_count = 0
    best = 0

    while l < len(stock):
        while r + 1 < len(stock) and (stock[r + 1] == 1 or zero_count < 1):
            if stock[r + 1] == 0:
                zero_count += 1
            r += 1

        best = max(best, r - l + 1)

        if stock[l] == 0:
            zero_count -= 1
        l += 1

    return best

if __name__ == "__main__":
    ex1 = [1,1,0,1,1,1,1,0,1]
    ex2 = [0]
    ex3 = [1,0,0,1]

    ans1 = longest_stock_growth(ex1)
    ans2 = longest_stock_growth(ex2)
    ans3 = longest_stock_growth(ex3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина массива stock
Память: O(1)
"""