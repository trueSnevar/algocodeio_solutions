"""
Вид справа

легко
решено

Дан корень бинарного дерева.
Нужно вернуть массив значений, где каждое значение соответствует самой правой вершине уровня дерева

ВАЖНО: реши задачу с использованием рекурсии


Пример 1:

Ввод: root = [1,2,3,6,4,null,null,8]
Вывод: [1,3,4,8]

Пример 2:

Ввод: root = [5]
Вывод: [5]

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
#     5


root2 = TreeNode(5)


def right_side_view(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque([root])

    while q:
        res.append(q[-1].val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

def right_side_view_recursive(root: Optional[TreeNode]) -> List[int]:
    res = []
    def traverse(node: TreeNode, level: int) -> None:
        if not node:
            return
        if level == len(res):
            res.append(0)
        res[level] = node.val # просто перезаписываем вершину
        traverse(node.left, level + 1)
        traverse(node.right, level + 1)
    traverse(root, 0)
    return res

if __name__ == "__main__":
    ans1 = right_side_view(root1)
    ans2 = right_side_view(root2)

    ans3 = right_side_view_recursive(root1)
    ans4 = right_side_view_recursive(root2)

    print(ans1)
    print(ans2)

    print(f"Recursive: {ans3}")
    print(f"Recursive: {ans4}")

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(n+h), где n - число вершин в дереве; h - высота дерева
"""