"""
Пересечение отрезков

средне
решено

Даны два отсортированных массива не пересекающихся отрезков segments1 и segments2,
где каждый отрезок представлен в виде [начало, конец].
Нужно вернуть массив пересечений отрезков из segments1 и segments2.

Пример 1:

Ввод: segments1 = [[2,4],[5,6],[7,9],[10,12]]
segments2 = [[3,7],[10,12],[13,14]]
Вывод: [[3,4],[5,6],[7,7],[10,12]]

Пример 2:

Ввод: segments1 = [[1,3],[5,8]]
segments2 = [[2,4],[6,7]]
Вывод: [[2,3],[6,7]]

Ограничения:

len(segments1) + len(segments2) >= 1
"""

from typing import *


# проверяем пересекаются ли интервалы
def is_overlapping(a: List[int], b: List[int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


# интервалы обязательно должны пересекаться
def overlap_two_segments(a: List[int], b: List[int]) -> List[int]:
    return [max(a[0], b[0]), min(a[1], b[1])]


def intersect(segments1: List[List[int]], segments2: List[List[int]]) -> List[List[int]]:
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(segments1) and p2 < len(segments2):
        # если пересекаются - добавляем в ответ
        if is_overlapping(segments1[p1], segments2[p2]):
            result.append(overlap_two_segments(segments1[p1], segments2[p2]))

        # важно сравнивать именно концы интервалов, а не начало
        if segments1[p1][1] < segments2[p2][1]:
            p1 += 1
        else:
            p2 += 1
    return result


if __name__ == "__main__":
    ex1 = [[2,4],[5,6],[7,9],[10,12]]
    ex2 = [[3,7],[10,12],[13,14]]

    ex3 = [[1,3],[5,8]]
    ex4 = [[2,4],[6,7]]
    ans1 = intersect(ex1, ex2)
    ans2 = intersect(ex3, ex4)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(n*log(n)), где n - длина массива segments
Память: O(1), при условии, что сортировка не будет использовать дополнительную память
"""