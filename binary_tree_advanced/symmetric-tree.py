"""
Симметричное дерево

легко
решено

Дан корень бинарного дерева. Нужно проверить, является ли дерево симметричным

ВАЖНО: реализуй обход с использованием рекурсии

Пример 1:



Ввод: root = [2,5,5,1,8,8,1,null,null,3,null,null,3]
Вывод: true
Объяснение: Дерево симметрично, потому что левое и правое поддерево корня симметричны

           2
         /   \
        5     5
       / \   / \
      1   8 8   1
         /   \
        3     3


Пример 2:

Ввод: root = [1,2,2,null,3,null,3]

      1
     / \
    2   2
     \   \
      3   3

Вывод: false

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



root1 = TreeNode(
    2,
    TreeNode(
        5,
        TreeNode(1),
        TreeNode(
            8,
            TreeNode(3),
            None
        )
    ),
    TreeNode(
        5,
        TreeNode(
            8,
            None,
            TreeNode(3)
        ),
        TreeNode(1)
    )
)

root2 = TreeNode(
    1,
    TreeNode(
        2,
        None,
        TreeNode(3)
    ),
    TreeNode(
        2,
        None,
        TreeNode(3)
    )
)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def dfs(left, right):
        if not left and not right:
            return True

        if not left and right or left and not right:
            return False

        return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


if __name__ == "__main__":
    ans1 = is_symmetric(root1)
    ans2 = is_symmetric(root2)

    print(ans1)
    print(ans2)


"""
Оценка сложности

Время: O(min(n1, n2)), где n1 - число вершин в первом поддереве; n2 - число вершин во втором поддереве
Память: O(min(h1, h2)), где h1 - высота первого поддерева; h2 - высота второго поддерева
"""