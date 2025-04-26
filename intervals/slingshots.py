"""
Выстрелы из рогатки
средне
решено

На полу расположены несколько воздушных шаров.
Каждый i-ый шар можно расположить в отрезке points[i],
где points[i][0] — начало, а points[i][1] — конец отрезка.

Петя стреляет из рогатки строго параллельно полу.
Нужно найти минимальное количество выстрелов, чтобы лопнуть все шары.

Пример 1:

Ввод: points = [[1,5],[8,12],[0,3],[6,8],[7,8]]
Вывод: 2
Объяснение: Первым выстрелом сбиваем [1,5] и [0,3], а вторым [8,12],[6,8],[7,8].

Пример 2:

Ввод: points = [[2,17],[100,160]]
Вывод: 2

Ограничения:

len(points) >= 1
"""

from typing import *

# проверяем пересекаются ли интервалы
def is_overlapping(a: List[int], b: List[int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])

# интервалы обязательно должны пересекаться
def overlap_two_intervals(a: List[int], b: List[int]) -> List[int]:
    return [max(a[0], b[0]), min(a[1], b[1])]

def count_shots(points: List[List[int]]) -> int:
    points.sort()
    result = 1
    last_point = points[0]
    for point in points:
        # если интервалы пересекаются, то для них используем 1 выстрел
        # и стараемся набрать как можно больше интервалов под 1 выстрел
        if is_overlapping(last_point, point):
            last_point = overlap_two_intervals(last_point, point)
            continue
        # если нет пересечений значит нужна еще 1 доп выстрел и обновляем
        # последний интервал (last_point)
        last_point = point
        result += 1
    return result


if __name__ == "__main__":
    ex1 = [[1,5],[8,12],[0,3],[6,8],[7,8]]
    ex2 = [[2,17],[100,160]]
    ans1 = count_shots(ex1)
    ans2 = count_shots(ex2)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(n*log(n)), где n - длина массива points
Память: O(1), при условии, что сортировка не выделяет доп.память
"""