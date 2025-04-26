"""
Под боем королевы

средне
решено

Дан двухмерный массив целых чисел board.

Нужно найти максимальную сумму клеток, которые бьет шахматная королева,
если поставить ее на доску, включая клетку с самой королевой.

Пример 1:

Ввод: board =
[[3,2,5,1]
,[4,9,1,3]
,[2,9,2,1]]
Вывод: 40
Объяснение: получим сумму 40 если поставить ладью на клетку [1,1] (индексация с 0).

Пример 2:

Ввод: board = [[1,2,3]]
Вывод: 6
Ограничения:

len(board[i]) >= 1
"""

from typing import *


def max_queen_sum(board: List[List[int]]) -> int:
    # rows_sum[i] - будет содержать сумму всех элементов для i-ой строки
    rows_sum = [0] * len(board)
    # cols_sum[i] - будет содержать сумму всех элементов для i-ой колонки
    cols_sum = [0] * len(board[0])
    # d1_sum, d2_sum - содержитат сумму элементов на диагоналях
    d1_sum = [0] * (len(board) + len(board[0]) - 1)
    d2_sum = [0] * (len(board) + len(board[0]) - 1)
    # делам предпосчет, чтобы быстро находить позицию
    for i in range(len(board)):
        for j in range(len(board[i])):
            val = board[i][j]
            rows_sum[i] += val
            cols_sum[j] += val
            d1_sum[i - j + len(board[0]) - 1] += val
            d2_sum[i + j] += val

    max_sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            # при подсчете суммы складываем сумму текущей строки, столбца,
            #  двух диагоналей и не забываем вычитать общий серединный элемент
            curr_sum = rows_sum[i] + cols_sum[j]
            curr_sum += d1_sum[i - j + len(board[0]) - 1] + d2_sum[i + j]
            curr_sum -= 3 * board[i][j]
            # обновляем максимальную сумму
            if i == 0 and j == 0:
                # сумма может быть меньше 0, поэтому
                # важно инициализировать начальным значением
                max_sum = curr_sum
            max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    ex1 = [
        [3,2,5,1],
        [4,9,1,3],
        [2,9,2,1]
    ]
    ex2 = [[1,2,3]]

    ans1 = max_queen_sum(ex1)
    ans2 = max_queen_sum(ex2)
    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n*m), где n*m - число элементов в двухмерном массиве board
Память: O(n*m), где n*m - число элементов в двухмерном массиве board
"""