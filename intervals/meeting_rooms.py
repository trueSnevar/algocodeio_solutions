"""
Число переговорок

средне
решено

Дан массив отрезков segments, где segments[i] содержит отрезок бронирования комнаты для переговоров:
[начало бронирования, конец бронирования].

Нужно вернуть минимальное число комнат для переговоров, которое должно быть, чтобы все переговоры могли состояться.

Пример 1:

Ввод: segments = [[2,5],[0,6],[0,3],[9,11],[5,8]]
Вывод: 3

Пример 2:

Ввод: segments = [[5,10],[11,14]]
Вывод: 1

Ограничения:

len(segments) >= 1
"""

from typing import *

def count_meeting_rooms(segments: List[List[int]]) -> int:
    points = []
    for elem in segments:
        points.append([elem[0], +1]) # точка, +1 - что нужна еще одна комната
        points.append([elem[1], -1]) # точка, -1 - что комната осободилась

    points.sort() # [10, -1] будет перед [10, +1] - сначала комнаты особождают а потом занимают
    max_room_numbers = 0
    curr_room_numbers = 0
    # для каждого момента времени находим используемое число комнат и выбираем максимальное значение
    for point in points:
        curr_room_numbers += point[1]
        max_room_numbers = max(max_room_numbers, curr_room_numbers)
    return max_room_numbers


if __name__ == "__main__":
    ex1 = [[2,5],[0,6],[0,3],[9,11],[5,8]]
    ex2 = [[5,10],[11,14]]
    ans1 = count_meeting_rooms(ex1)
    ans2 = count_meeting_rooms(ex2)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(n*log(n)), где n - длина массива segments
Память: O(n), где n - длина массива segments
"""