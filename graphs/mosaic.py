"""
Мозаика

легко
решено

Дана цветная мозаика в виде двумерного массива grid, где каждое число обозначает цвет клетки.
Нужно найти цвет, у которого максимальное количество компонент связности.
Гарантируется, что такой цвет единственный.

Один компонент связности - это группа соединённых клеток одного цвета,
которые соседствуют только по вертикали или горизонтали
(по диагонали клетки не считаются соединёнными).

Пример:

Ввод: grid =
[[8,8,2,2,1]
,[8,8,2,1,1]
,[2,2,2,2,1]
,[1,1,8,8,8]
,[1,8,8,1,8]]
Вывод: 1

Объяснение: у цвета "1" - 3 компоненты (наибольшее число компонент).

grid =  [1, 1, 1, 1, 1, 1, 1, 1]
        [1, 2, 2, 1, 1, 2, 2, 1]
        [1, 2, 1, 2, 2, 1, 2, 1]
        [1, 2, 2, 2, 2, 2, 2, 1]
        [1, 1, 1, 1, 1, 1, 1, 1];
Вывод: 1
"""

from typing import *
from collections import defaultdict

def max_components(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    freq = defaultdict(int)

    def dfs(r, c, needed_color):
        visited.add((r, c))
        for dr, dc in dirs:
            nr = dr + r
            nc = dc + c
            if (
                    nr in range(ROWS) and
                    nc in range(COLS) and
                    (nr, nc) not in visited and
                    grid[nr][nc] == needed_color
            ):
                dfs(nr, nc, grid[nr][nc])

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) not in visited:
                dfs(i, j, grid[i][j])
                freq[grid[i][j]] += 1

    max_color_count = max(freq.values())

    for color, fr in freq.items():
        if fr == max_color_count:
            return color

    return 0

if __name__ == "__main__":
    ex1 = [
          [8, 8, 2, 2, 1]
        , [8, 8, 2, 1, 1]
        , [2, 2, 2, 2, 1]
        , [1, 1, 8, 8, 8]
        , [1, 8, 8, 1, 8]
    ]

    ex2 =[
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 2, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]



    ans1 = max_components(ex1)
    ans2 = max_components(ex2)


    print(ans1)
    print(ans2)



"""
Оценка сложности

Время: O(n * m), где n кол-во строк и m кол-во столбцов входного массива
Память: O(n * m), где n кол-во строк и m кол-во столбцов входного массива
"""

