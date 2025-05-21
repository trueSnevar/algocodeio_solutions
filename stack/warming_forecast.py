"""
Прогноз потеплений

средне
решено

Дан массив temperature, где temperature[i] — температура в i-й день.
Нужно вернуть массив result, где result[i] — количество дней,
через которое температура станет выше, чем в i-й день.
Если потепления не будет, result[i] = 0.

Дни с одинаковой температурой не считаются потеплением.

Пример 1:

Ввод: temperature = [5,6,9,7,5,-1,8,11,2]
Вывод: [1,1,5,3,2,1,1,0,0]

Пример 2:

Ввод: temperature = [5,4,3]
Вывод: [0,0,0]

Пример 3:

Ввод: temperature = [2,3,4,5]
Вывод: [1,1,1,0]

Ограничения:

len(temperature) >= 1
"""

from typing import *

def predict_warming(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    # в стеке всегда храним номер дня
    stack = []
    for i, temperature in enumerate(temperatures):
        # пока текущая температура больше чем температура в стеке
        # вынимаем удаляем из стека элементы и
        # вычисляем для них ответ
        while len(stack) > 0 and temperatures[stack[-1]] < temperature:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

if __name__ == "__main__":
    ex1 = [5,6,9,7,5,-1,8,11,2] # [1,1,5,3,2,1,1,0,0]
    ex2 = [5,4,3] # [0,0,0]
    ex3 = [2,3,4,5] # [1,1,1,0]

    ans1 = predict_warming(ex1)
    ans2 = predict_warming(ex2)
    ans3 = predict_warming(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n), где n - размер массива temperatures
Память: O(n), где n - размер массива temperatures
"""

