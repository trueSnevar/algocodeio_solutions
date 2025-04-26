"""
Вместимость автобуса

средне
решено

Дан массив trips, где каждый элемент trips[i] = [from, to, passengers]
описывает поездку: from — точка посадки, to — точка высадки, passengers — количество пассажиров.
Также дано число capacity — максимальное количество пассажиров, которое может перевозить автобус.

Нужно вернуть true, если водитель автобуса сможет перевезти всех пассажиров, не превышая capacity,
и false в противном случае.

Пример 1:

Ввод: trips = [[1,5,2],[3,7,3]], capacity = 6
Вывод: true

Пример 2:

Ввод: trips = [[6,8,2],[1,4,3],[2,5,4]], capacity = 5
Вывод: false

Ограничения:

len(trips) >= 1
len(trips[i]) == 3
from >= 0
to > from
passengers >= 1
capacity >= 1

"""

from typing import *


def bus_capacity(trips: List[List[int]], capacity: int) -> bool:
    points = []
    for trip in trips:
        # Добавляем точку, где пассажиры заходят (from, passengers)
        points.append([trip[0], trip[2]])
        # Добавляем точку, где пассажиры выходят (to, -passengers)
        points.append([trip[1], -trip[2]])

    # Сортируем точки по координате
    # Если координаты равны, сначала обрабатываем выход пассажиров, затем вход
    points.sort(key=lambda x: (x[0], x[1]))

    curr_passengers = 0
    for point in points:
        # Обновляем текущее количество пассажиров
        curr_passengers += point[1]
        # Если превышена вместимость, возвращаем False
        if curr_passengers > capacity:
            return False

    # Если ни в одной точке не превышена вместимость, возвращаем True
    return True

if __name__ == "__main__":
    ex1 = [[1,5,2],[3,7,3]]
    capacity1 = 6

    ex2 = [[6,8,2],[1,4,3],[2,5,4]]
    capacity2 = 5
    ans1 = bus_capacity(ex1, capacity1)
    ans2 = bus_capacity(ex2, capacity2)
    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(n*log(n)), где n — количество поездок.
Память: O(n), так как мы храним список точек.
"""