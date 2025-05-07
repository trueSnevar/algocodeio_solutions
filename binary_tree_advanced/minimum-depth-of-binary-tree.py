"""
Минимальная глубина дерева

средне
решено

Дан корень бинарного дерева. Нужно вернуть минимальное число вершин между корнем
и одним из листов, включая в подсчет сам корень и лист.

ВАЖНО: используй рекурсивную реализацию

Пример 1:

Ввод: root = [1,2,3,4,5,null,6,null,null,7,8,null,14]
Вывод: 3

Схема:
             1
           /   \
          2     3
         / \     \
        4   5     6
           / \     \
          7   8     14

Минимальный путь: 1 -> 2 -> 4 (длина 3)

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
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значение вершин лежит в диапазоне [-10000, 10000]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:
    """
    Возвращает минимальное число вершин на пути от корня до ближайшего листа.
    """
    if not root:
        return 0
    depth = 1

    left = min_depth(root.left)
    right = min_depth(root.right)
    # если одно из поддеревьев пусто (глубина == 0), берём глубину другого
    if not left or not right:
        return depth + left + right
    # оба поддерева непусты — берём минимум
    return depth + min(left, right)


if __name__ == "__main__":
    # Пример 1
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
            TreeNode(
                6,
                None,
                TreeNode(14)
            )
        )
    )
    print(min_depth(root1))  # 3

    # Пример 2
    root2 = TreeNode(
        8,
        None,
        TreeNode(
            4,
            None,
            TreeNode(9)
        )
    )
    print(min_depth(root2))  # 3

# Оценка сложности:
# Время: O(n), где n — число узлов в дереве
# Память: O(h), где h — высота дерева (стек рекурсии)
