"""
Сумма листьев в дереве

легко
решено

Дан корень бинарного дерева. Нужно вернуть сумму всех листьев в дереве

ВАЖНО: реши задачу с использованием рекурсии


Пример 1:


Ввод: root = [1,2,3,4,5,null,6,null,null,7,8]
Вывод: 25

Объяснение: В дереве 4 листа со значениями [4,7,8,6], а их сумма 25

Пример 2:

Ввод: root = [10]
Вывод: 10
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


# возвращаем True если node - лист и False если не лист
def is_leaf(node: TreeNode) -> bool:
    # вершина - лист, если левый и правый ребенок отсутствуют
    return node.left is None and node.right is None

def leaves_sum(root: Optional[TreeNode]) -> int:
    # если вершина - пустая, то возвращаем 0
    if root is None:
        return 0
    # если вершина - лист, то возвращаем ее значение
    if is_leaf(root):
        return root.val
    # если вершина не лист - возвращаем сумму листов из левого и правого поддерева
    return leaves_sum(root.left) + leaves_sum(root.right)

if __name__ == "__main__":
    ans1 = leaves_sum(root1)
    ans2 = leaves_sum(root2)

    print(ans1)
    print(ans2)

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(h), где h - высота дерева
"""