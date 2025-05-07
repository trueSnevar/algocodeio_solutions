"""
Максимальная глубина дерева

легко
решено

Дан корень бинарного дерева. Нужно вернуть максимальное число вершин между корнем и одним из листов,
включая в подсчет сам корень и лист.

ВАЖНО: реализуй обход с использованием рекурсии

Пример 1:

Ввод: root = [1,2,3,4,5,null,6,null,null,7,8]
Вывод: 4

Схема:
             1
           /   \
          2     3
         / \     \
        4   5     6
           / \
          7   8

Пример 2:

Ввод: root = [8,null,4,null,null,9]
Вывод: 3

Схема:
        8
         \
          4
           \
            9

Ограничения:
- Число узлов в дереве >= 1
- Высота дерева <= 1000
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


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Возвращает максимальную глубину (число вершин) от корня до самого дальнего листа.
    """
    if not root:
        return 0

    depth = 1
    # Рекурсивно считаем глубину левого и правого поддеревьев и берём максимум
    left = max_depth(root.left)
    right = max_depth(root.right)

    depth += max(left, right)

    return depth


if __name__ == "__main__":
    # Пример 1
    root1 = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5, TreeNode(7), TreeNode(8))
        ),
        TreeNode(3, None, TreeNode(6))
    )
    print(max_depth(root1))  # 4

    # Пример 2
    root2 = TreeNode(
        8,
        None,
        TreeNode(4, None, TreeNode(9))
    )
    print(max_depth(root2))  # 3

# Оценка сложности:
# Время: O(n), где n — число узлов в дереве
# Память: O(h), где h — высота дерева (глубина рекурсии)
