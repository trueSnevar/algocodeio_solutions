"""
Слияние отрезков

средне
решено

Дан массив отрезков segments, где каждый отрезок представлен в виде [начало, конец].
Нужно объединить все пересекающиеся отрезки и вернуть массив непересекающихся отрезков,
отсортированных по возрастанию.

Отрезки считаются пересекающимися, если у них есть хотя бы одна общая точка.

Пример 1:

Ввод: segments = [[2,5],[0,6],[0,3],[9,11],[6,8]]
Вывод: [[0,8],[9,11]]

Пример 2:

Ввод: segments = [[1,2],[3,3],[100,150]]
Вывод: [[1,2],[3,3],[100,150]]

Ограничения:

len(segments) >= 1
конец >= начало >= 0
"""

from typing import *

def is_overlapping(a: int, b: int) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])

def merge_two_segments(a: int, b: int) -> List[int]:
    # интервалы обязательно должны пересекаться
    return [a[0], max(a[1], b[1])]

def merge(segments: List[List[int]]) -> List[List[int]]:
    segments.sort()

    result = []
    result.append(segments[0])

    for i in range(1, len(segments)):
        segment = segments[i]
        # если текущий интервал и последний в ответе пересекаются,
        # значит объединяем их, иначе добавляем интервал к ответу и это значит,
        # что ни один интервал, который имеет точку начала меньше текущего интервала
        # не будет пересечен ни с одним лежащим правее и не с текущим
        if is_overlapping(result[-1], segment):
            result[-1] = merge_two_segments(result[-1], segment)
        else:
            result.append(segment)
    return result


if __name__ == "__main__":
    ex1 = [[2,5],[0,6],[0,3],[9,11],[6,8]]
    ex2 = [[1,2],[3,3],[100,150]]
    ans1 = merge(ex1)
    ans2 = merge(ex2)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(n*log(n)), где n - длина массива segments
Память: O(n), где n - длина массива segments
"""