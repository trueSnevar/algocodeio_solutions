"""
Сбалансированное дерево

средне
решено

Дан корень бинарного дерева и нужно вернуть True, если дерево сбалансированно по высоте, и False в обратном.

Дерево считается сбалансированным по высоте, если для каждой вершины высота левого и правого поддерева
не отличаются больше чем на 1.

ВАЖНО: используй рекурсивную реализацию

Пример 1:

Ввод: root = [1,3,2,4,5,null,null,7,8]
Вывод: False

Схема:
             1
           /   \
          3     2
         / \
        4   5
       / \
      7   8

Пример 2:

Ввод: root = [3,9,20,null,null,15,7]
Вывод: True

Схема:
        3
       / \
      9   20
         /  \
        15   7

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значение вершин дерева лежит в диапазоне [-10000, 10000]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Проверяет, сбалансировано ли дерево по высоте.
    """
    def dfs(node):
        if not node:
            return 0

        # находим глубину левого поддерева
        # если глубина = -1 значит поддерево не сбалансировано,
        # а значит и все дерево не сбалансированно
        left = dfs(node.left)
        if left == -1:
            return -1

        # находим глубину правого поддерева
        right = dfs(node.right)
        if right == -1:
            return -1

        # если разница глубин > 1, то дерево не сбалансированно
        if abs(left - right) > 1:
            return -1

        # считаем глубину
        return 1 + max(left, right)

    return dfs(root) != -1


if __name__ == "__main__":
    # Пример 1
    root1 = TreeNode(
        1,
        TreeNode(
            3,
            TreeNode(
                4,
                TreeNode(7),
                TreeNode(8)
            ),
            TreeNode(5)
        ),
        TreeNode(2)
    )
    print(is_balanced(root1))  # False

    # Пример 2
    root2 = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    print(is_balanced(root2))  # True

# Оценка сложности:
# Время: O(n), где n — число узлов в дереве
# Память: O(h), где h — высота дерева (глубина рекурсии)
