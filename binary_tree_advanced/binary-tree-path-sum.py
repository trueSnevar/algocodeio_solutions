"""
Сумма от корня до листа

средне
решено

Дан корень бинарного дерева и targetSum. Нужно проверить, существует ли путь от корня до листа (включая и лист,
и корень), сумма вершин на котором равна targetSum.
Переходить от одного узла к другому можно только сверху вниз (т.е. от родителя к ребенку).

ВАЖНО: реализовать задачу с использованием рекурсии

Пример 1:

Ввод: root = [1,2,3,3,4,null,6,null,null,1,1,null,5], targetSum = 22
Вывод: True

Схема:
             1
           /   \
          2     3
         / \     \
        3   4     6
           / \     \
          1   1     5

— существует путь 1→2→4→1 (сумма 8) и 1→3→6→5 (сумма 15) — но верный путь 1→2→3 (sum 6)?
  Правильнее: путь 1→2→4→15? Нет, исходный пример: 1→2→4→1=8 !=22. Ошибка.
  Скорее: 1→2→3→... пример не соответствует.
  Исправим: пусть путь 1→2→4→1=8, пример не соответствует условию.
  Вместо этого возьмём стандартный пример: [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum=22.

Пример 1 (корректный):
Ввод: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Вывод: True

Схема:
               5
             /   \
            4     8
           /     / \
         11     13  4
        /  \         \
       7    2         1

— путь 5→4→11→2 даёт сумму 22.

Пример 2:

Ввод: root = [1,2,3], targetSum = 5
Вывод: False

Схема:
     1
    / \
   2   3

— возможные суммы: 1→2=3, 1→3=4.

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значения вершин в диапазоне [-10000, 10000]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    Возвращает True, если в дереве существует путь от корня до листа с суммой targetSum.
    """
    def dfs(node: Optional[TreeNode], remaining: int) -> bool:
        if not node:
            return False
        remaining -= node.val
        # если достигли листа — проверяем, равен ли остаток нулю
        if not node.left and not node.right:
            return remaining == 0
        # иначе проверяем поддеревья
        return dfs(node.left, remaining) or dfs(node.right, remaining)

    return dfs(root, targetSum)


if __name__ == "__main__":
    # Пример 1
    root1 = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                None,
                TreeNode(1)
            )
        )
    )
    print(has_path_sum(root1, 22))  # True

    # Пример 2
    root2 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    print(has_path_sum(root2, 5))   # False

# Оценка сложности:
# Время: O(n), где n — число узлов в дереве
# Память: O(h), где h — высота дерева (глубина рекурсии)
