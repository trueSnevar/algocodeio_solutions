"""
Сумма правых листьев дерева

легко
решено

Дан корень бинарного дерева. Нужно вернуть сумму всех правых листьев в дереве.
Если правых листьев нет, то нужно вернуть ноль

ВАЖНО: реши задачу с использованием рекурсии

Пример 1:

Ввод: root = [1,2,3,4,5,null,6,null,null,7,8]
Вывод: 14
Объяснение: в дереве 2 правых листа со значениями [8,6], а их сумма 14

Пример 2:

Ввод: root = [10]
Вывод: 0
Объяснение: корень дерева не является ни правой ни левой вершиной

Ограничения:

Число узлов в дереве >= 1
Высота дерева <= 1000
Значение вершин дерева лежит в диапазоне [-10 000, 10 000] (включительно)
"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Строим дерево из списка [1,2,3,4,5,null,6,null,null,7,8]:
#
#            1
#          /   \
#         2     3
#        / \     \
#       4   5     6
#          / \
#         7   8
#

root1 = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(4),
        TreeNode(
            5,
            TreeNode(7),
            TreeNode(8)
        )
    ),
    TreeNode(
        3,
        None,
        TreeNode(6)
    )
)

#
#     10


root2 = TreeNode(10)


def sum_of_right_leaves(root: Optional[TreeNode]) -> int:
    def traverse(node: Optional[TreeNode], is_right: bool) -> int:
        if not node:
            return 0

        _sum = 0

        if not node.left and not node.right and is_right:
            _sum += node.val

        _sum += traverse(node.left, False) + traverse(node.right, True)
        return _sum

    return traverse(root, False)


if __name__ == "__main__":
    ans1 = sum_of_right_leaves(root1)
    ans2 = sum_of_right_leaves(root2)

    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(h), где h - высота дерева
"""