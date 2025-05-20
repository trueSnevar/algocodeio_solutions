"""
Сжатие значений счетчика

средне
решено

Дан отсортированный по возрастанию массив уникальных чисел counter, где counter[i] — значение метрики в i-ю секунду.

Чтобы упростить восприятие, нужно сжать последовательность,
объединяя подряд идущие числа например: [1,2,3,7] -> ["1->3","7"]:

Если числа идут подряд (разница = 1), записать в виде "x->y".
В остальных случаях оставить как есть ("x").

Пример 1:

Ввод: сounter = [1,2,3,4,5,8,10,15,16,20]
Вывод: ["1->5","8","10","15->16","20"]

Пример 2:

Ввод: сounter = [-3,-2]
Вывод: ["-3->-2"]

Пример 3:

Ввод: сounter = [0,2,4,6]
Вывод: ["0","2","4","6"]

Ограничения:

0 <= len(сounter)
"""

from typing import *


def counter_ranges(counter: List[int]) -> List[str]:
    l = 0
    r = 0
    result = []
    while l < len(counter):
        while r + 1 < len(counter) and counter[r] + 1 == counter[r + 1]:
            r += 1

        if r != l:
            result.append(f'{counter[l]}->{counter[r]}')
        else:
            result.append(f'{counter[l]}')

        l = r + 1
        r = r + 1
    return result

if __name__ == "__main__":
    ex1 = [1,2,3,4,5,8,10,15,16,20]
    ex2 = [-3,-2]
    ex3 = [0,2,4,6]

    ans1 = counter_ranges(ex1) # ["1->5","8","10","15->16","20"]
    ans2 = counter_ranges(ex2) # ["-3->-2"]
    ans3 = counter_ranges(ex3) # ["0","2","4","6"]
    print(ans1)
    print(ans2)
    print(ans3)

"""
Оценка сложности

Время: O(n), где n - длина массива counter
Память: O(n), где n - длина массива counter
"""