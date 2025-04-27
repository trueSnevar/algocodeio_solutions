"""
Поиск в 2D массиве

средне
решено

Дан двумерный массив matrix размером n x m, где каждая строка отсортирована в монотонно возрастающем порядке,
а первый элемент каждой строки строго больше последнего элемента предыдущей строки.
Также дано число target. Нужно вернуть true, если target присутствует в matrix, и false в противном случае.

Пример 1:

Ввод: matrix =
[[1,2,3]
,[4,5,6]
,[7,8,9]], target = 6
Вывод: true

Пример 2:

Ввод: matrix =
[[11,25,31]
,[49,56,68]
,[72,87,90]], target = 22
Вывод: false

Ограничения:

len(matrix) >= 1

"""

from typing import *

def search(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    l = 0
    r = rows * cols

    while r - l > 1:
        mid = (r + l) // 2
        cur_row = mid // cols
        cur_col = mid % cols
        if matrix[cur_row][cur_col] <= target:
            l = mid
        else:
            r = mid
    return matrix[l//cols][l%cols] == target


if __name__ == "__main__":
    ex1 = [[1,2,3],[4,5,6],[7,8,9]]
    target1 = 6

    ex2 = [[11, 25, 31]
        , [49, 56, 68]
        , [72, 87, 90]]
    target2 = 22

    ans1 = search(ex1, target1)
    ans2 = search(ex2, target2)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(log(n)), где n - длина массива nums
Память: O(1)
"""