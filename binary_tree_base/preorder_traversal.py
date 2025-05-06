"""
Прямой обход

легко
решено

Дан корень бинарного дерева. Нужно вернуть значения узлов в прямом порядке


Алгоритм прямого обхода:

1. Если текущий узел пустой - возвращаемся в родительскую вершину
2. Добавляем значение текущего узла в ответ
3. Обходим левое поддерево рекурсивно
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


#        1
#      /   \
#     2     6
#    / \     \
#   3   5     7
#  /
# 4

root1 = TreeNode(1,
                TreeNode(2,
                         TreeNode(3,
                                  TreeNode(4),  # левый ребёнок 3
                                  None
                                  ),
                         TreeNode(5)  # правый ребёнок 2
                         ),
                TreeNode(6,
                         None,
                         TreeNode(7)  # правый ребёнок 6
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


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res

def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    res = []
    def preorder(node: TreeNode):
        if not node:
            return
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return res

if __name__ == "__main__":
    ans1 = preorder_traversal(root1) # Вывод: [1,2,3,4,5,6,7]
    ans2 = preorder_traversal(root2) # Вывод: [8,4,9]

    ans3 = preorder_traversal_recursive(root1) # Вывод: [1,2,3,4,5,6,7]
    ans4 = preorder_traversal_recursive(root2) # Вывод: [8,4,9]

    print(ans1)
    print(ans2)

    print(f"Recursive: {ans3}")
    print(f"Recursive: {ans4}")

"""
Оценка сложности

Время: O(n), где n - число вершин в дереве
Память: O(n+h), где n - число вершин в дереве; h - высота дерева
"""