"""
Три в ряд

средне
решено

Дан массив чисел colors, где colors[i] — цвет шара на позиции i.
Если три или более шаров одного цвета стоят подряд, они схлопываются.
Нужно вернуть общее количество шаров, которые схлопнутся.

После схлопывания шаров, оставшиеся шары могут снова образовать последовательность из трёх
или более одинаковых цветов, что также приведёт к их схлопыванию.

Пример 1:

Ввод: colors = [1,1,2,2,2,1]
Вывод: 6
Объяснение: сначала схлопнутся двойки, а потом единички

Пример 2:

Ввод: colors = [4,1,2,3,3,3,2,2,1,1]
Вывод: 9

Пример 3:

Ввод: colors = [1,2,3]
Вывод: 0

Ограничения:

len(colors) >= 1
"""

from typing import *

def play(nums: List[int]) -> int:
    stack = []
    result = 0
    for num in nums:
        if len(stack) >= 2 and stack[-1] == num and stack[-2] == num:
            # если три подряд одинаковых, схлопываем
            result += 3
            stack.pop()
            stack.pop()
            continue
        stack.append(num)
    return result

if __name__ == "__main__":
    ex1 = [1,1,2,2,2,1] # 6
    ex2 = [4,1,2,3,3,3,2,2,1,1] # 9
    ex3 = [1,2,3] # 0

    ans1 = play(ex1)
    ans2 = play(ex2)
    ans3 = play(ex3)

    print(ans1)
    print(ans2)
    print(ans3)



"""
Оценка сложности

Время: O(n), где n - размер массива nums
Память: O(n), где n - размер массива nums
"""

