"""
Центрированный обход

легко
решено

Дан корень бинарного дерева. Нужно вернуть значения узлов в центрированном порядке


Алгоритм центрированного обхода:

1. Если текущий узел пустой - возвращаемся в родительскую вершину
2. Обходим левое поддерево рекурсивно
3. Добавляем значение текущего узла в ответ
4. Обходим правое поддерево рекурсивно
5. Возвращаемся в родительскую вершину

ВАЖНО: реализуй обход с использованием рекурсии
"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#
#         5
#        / \
#       3   6
#      / \   \
#     2   4   7
#    /
#   1

root1 = TreeNode(
    5,
    TreeNode(
        3,
        TreeNode(
            2,
            TreeNode(1),  # левый ребёнок 2
            None
        ),
        TreeNode(4)      # правый ребёнок 3
    ),
    TreeNode(
        6,
        None,
        TreeNode(7)      # правый ребёнок 6
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


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        node = stack.pop()
        res.append(node.val)
        curr = node.right
    return res

def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    res = []
    def inorder(node: TreeNode):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res

if __name__ == "__main__":
    ans1 = inorder_traversal(root1) # Вывод: [1,2,3,4,5,6,7]
    ans2 = inorder_traversal(root2) # Вывод: [8,4,9]

    ans3 = inorder_traversal_recursive(root1) # Вывод: [1,2,3,4,5,6,7]
    ans4 = inorder_traversal_recursive(root2) # Вывод: [8,4,9]

    print(ans1)
    print(ans2)

    print(f"Recursive: {ans3}")
    print(f"Recursive: {ans4}")

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(n+h), где n - число вершин в дереве; h - высота дерева
"""