"""
Обход по уровням

легко
решено

Дан корень бинарного дерева.
Нужно вернуть значения всех узлов по уровням (слева-направо и сверху-вниз)

ВАЖНО: реши задачу с использованием рекурсии

Пример 1:


Ввод: root = [1,2,3,4,5,null,6,null,null,7,8]
Вывод: [[1],[2,3],[4,5,6],[7,8]]
Объяснение: для каждого уровня используется отдельный массив,
поэтому возвращается массив массивов

Пример 2:

Ввод: root = [8,null,4,null,null,9]
Вывод: [[8],[4],[9]]

Ограничения:

Число узлов в дереве >= 1
Высота дерева <= 1000
Значение вершин дерева лежит в диапазоне [-10 000, 10 000] (включительно)
"""
from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
#     8
#      \
#       4
#        \
#         9
#

root2 = TreeNode(
    8,
    None,
    TreeNode(
        4,
        None,
        TreeNode(9)
    )
)


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque([root])

    while q:
        curr = []
        for _ in range(len(q)):
            node = q.popleft()
            curr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curr)
    return res

def level_order_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    res = []
    def traverse(node: TreeNode, level: int) -> None:
        if not node:
            return
        if level == len(res):
            res.append([])
        res[level].append(node.val)
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)
    traverse(root, 0)
    return res

if __name__ == "__main__":
    ans1 = level_order_traversal(root1)
    ans2 = level_order_traversal(root2)

    ans3 = level_order_traversal_recursive(root1)
    ans4 = level_order_traversal_recursive(root2)

    print(ans1)
    print(ans2)

    print(f"Recursive: {ans3}")
    print(f"Recursive: {ans4}")

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(n+h), где n - число вершин в дереве; h - высота дерева
"""