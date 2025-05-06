"""
Обход дерева зигзагом

легко
решено

Дан корень бинарного дерева. Нужно вернуть значения всех узлов загзагом по уровням

ВАЖНО: реши задачу с использованием рекурсии


Пример 1:

Ввод: root = [1,2,3,4,5,null,6,null,null,7,8]
Вывод: [[1],[3,2],[4,5,6],[8,7]]

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


def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque([(root, 0)])

    while q:
        curr = deque([])
        for _ in range(len(q)):
            node, lvl = q.popleft()
            if lvl % 2 == 0:
                curr.append(node.val)
            else:
                curr.appendleft(node.val)
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))
        res.append(list(curr))
    return res


def zigzag_level_order_recursive(root: Optional[TreeNode]) -> List[int]:
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
    for i in range(1, len(res), 2):
        res[i].reverse()
    return res

if __name__ == "__main__":
    ans1 = zigzag_level_order(root1)

    ans3 = zigzag_level_order_recursive(root1)

    print(ans1)

    print(f"Recursive: {ans3}")

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(n+h), где n - число вершин в дереве; h - высота дерева
"""