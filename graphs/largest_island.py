"""
Самый большой остров

средне
решено

Дана карта в виде двумерного массива grid из 0 и 1, где 1 обозначает сушу, а 0 обозначает воду.

Остров — это группа соединённых клеток с сушей (1),
 которые соседствуют только по вертикали или горизонтали
 (по диагонали клетки не считаются соединёнными).
 Cуша, прилегающая к границе карты, также считается островом.

Нужно найти площадь самого большого острова в массиве.
Если островов нет, верните 0.
Площадь острова — это количество единиц в этом острове.

Пример 1:

Ввод: grid =
[[1,0,0,0]
,[1,1,0,0]
,[0,1,0,0]
,[0,0,1,0]
,[0,0,0,0]]
Вывод: 4

Пример 2:

Ввод: grid =
[[0,0,0]
,[0,0,0]]
Вывод: 0

Ограничения:

len(grid) >= 1
len(grid[i]) >= 1
"""

from typing import *
from collections import defaultdict


def largest_island(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()

    def dfs(r, c):
        if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r, c) in visited or
                grid[r][c] == 0
        ):
            return 0

        visited.add((r, c))
        area = 1
        for dr, dc in dirs:
            nr = dr + r
            nc = dc + c
            area += dfs(nr, nc)
        return area

    ans = 0
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited and grid[i][j] == 1:
                ans = max(ans, dfs(i, j))

    return ans

if __name__ == "__main__":
    ex1 = [
          [1, 0, 0, 0]
        , [1, 1, 0, 0]
        , [0, 1, 0, 0]
        , [0, 0, 1, 0]
        , [0, 0, 0, 0]
    ]

    ex2 =[
          [0, 0, 0]
        , [0, 0, 0]
    ]



    ans1 = largest_island(ex1)
    ans2 = largest_island(ex2)


    print(ans1)
    print(ans2)



"""
Оценка сложности

Время: O(n * m), где n кол-во строк и m кол-во столбцов входного массива
Память: O(n * m), где n кол-во строк и m кол-во столбцов входного массива
"""

