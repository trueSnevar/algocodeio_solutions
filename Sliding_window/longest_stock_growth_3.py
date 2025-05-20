"""
Наглый подставной отчет
средне
решено
Дан массив stock, где stock[i] = 1 означает рост акций в i-й день, а stock[i] = 0 — падение.

Компания терпит убытки и готовит подставной отчет для инвесторов, в котором можно улучшить показатели,
заменив до k дней падения (0) на рост (1).

Требуется найти максимальное количество подряд идущих дней роста акций с учетом такой замены.

Нумерация в массиве начинается с единицы, а не с нуля.

Пример 1:

Ввод: stock = [1,0,1,1,0,1,1,0], k = 2
Вывод: 7
Объяснение: самый долгий рост акций с 1 по 7 день с заменой в 2 и 5 днях.

Пример 2:

Ввод: stock = [1,0,0,1], k = 1
Вывод: 2

Пример 3:

Ввод: stock = [0], k = 0
Вывод: 0

Ограничения:

0 <= len(stock)
Значение массива stock : 0 или 1
"""

from typing import *


def longest_stock_growth(stock: List[int], k: int) -> int:
    l = 0
    r = -1
    zero_count = 0
    best = 0

    while l < len(stock):
        while r + 1 < len(stock) and (stock[r + 1] == 1 or zero_count < k):
            if stock[r + 1] == 0:
                zero_count += 1
            r += 1

        best = max(best, r - l + 1)

        if stock[l] == 0:
            zero_count -= 1
        l += 1

    return best

if __name__ == "__main__":
    ex1 = [1,0,1,1,0,1,1,0] # 7
    k1 = 2

    ex2 = [0] # 0
    k2 = 0

    ex3 = [1,0,0,1] # 2
    k3 = 1

    ans1 = longest_stock_growth(ex1, k1)
    ans2 = longest_stock_growth(ex2, k2)
    ans3 = longest_stock_growth(ex3, k3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина массива stock
Память: O(1)
"""