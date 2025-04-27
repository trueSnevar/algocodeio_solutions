"""
Поиск первой и последней позиции

средне
решено

Дан массив nums, отсортированный в неубывающем порядке, и число target.
Нужно вернуть начальную и конечную позицию числа target в массиве nums.
Если число target отсутствует, вернуть [-1, -1].

Пример 1:

Ввод: nums = [1,2,2,2,2,2,5,5,8,19], target = 2
Вывод: [1,5]
Объяснение: индексация элементов начинается с нуля

Пример 2:

Ввод: nums = [1,3,4,6,7], target = 5
Вывод: [-1,-1]

Пример 3:

Ввод: nums = [1,3,5], target = 5
Вывод: [2,2]

Ограничения:

len(nums) >= 1

"""

from typing import *

def search_last_target(nums: List[int], target: int) -> int:
    # ответ будет находиться в элементе, указывающим на l
    # поэтому сдвигаем r на 1 вправо, чтобы l мог принимать
    # значения [0, len(nums) - 1] т е от первого и до последнего
    # индекса включительно
    l, r = 0, len(nums)
    while r - l > 1:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m
        else:
            r = m
    return l if nums[l] == target else -1

def search_first_target(nums: List[int], target: int) -> int:
    # ответ будет находиться в элементе указывающим на r
    # поэтому сдвигаем l на 1 влево, чтобы r мог принимать
    # значения [0, len(nums) - 1] т е от первого и до последнего
    # индекса включительно
    l, r = -1, len(nums) - 1
    while r - l > 1:
        m = (l + r) // 2
        if nums[m] < target:
            l = m
        else:
            r = m
    return r if nums[r] == target else -1

def search(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return [-1, -1]
    l = search_first_target(nums, target)
    r = search_last_target(nums, target)
    return [l, r]

if __name__ == "__main__":
    ex1 = [1,2,2,2,2,2,5,5,8,19]
    target1 = 2

    ex2 = [1,3,4,6,7]
    target2 = 5

    ex3 = [1,3,5]
    target3 = 5

    ans1 = search(ex1, target1)
    ans2 = search(ex2, target2)
    ans3 = search(ex3, target3)
    print(ans1)
    print(ans2)
    print(ans3)


"""
Оценка сложности

Время: O(log(n)), где n - длина массива nums
Память: O(1)
"""