"""
Идентичные деревья

легко
решено

Даны корни двух бинарных деревьев. Нужно проверить, являются ли деревья одинаковыми.
Деревья являются одинаковыми, если имеют одинаковую структуру и узлы имеют одинаковое значение.

ВАЖНО: реализуй обход с использованием рекурсии

Пример 1:

Ввод: p = [5,3,6,null,null,4,7], q = [5,3,6,null,null,4,7]
Вывод: True

Схема:
           5
         /   \
        3     6
             / \
            4   7

Пример 2:

Ввод: p = [1,2], q = [1,null,2]
Вывод: False

Схема:
    p:    1      q:  1
         /           \
        2             2

Пример 3:

Ввод: p = [1,2,1], q = [1,1,2]
Вывод: False

Схема:
    p:    1        q:    1
         / \           / \
        2   1         1   2

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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Рекурсивно сравнивает два дерева.
    Возвращает True, если они полностью идентичны.
    """
    # Если обе пусты — одинаковы
    if not p and not q:
        return True
    # Если один пуст, а другой нет — не одинаковы
    if not p or not q:
        return False
    # Значения корней должны совпадать, и поддеревья тоже
    left = is_same_tree(p.left, q.left)
    right = is_same_tree(p.right, q.right)
    return p.val == q.val and left and right


if __name__ == "__main__":
    # Пример 1
    p1 = TreeNode(5,
        TreeNode(3),
        TreeNode(6,
            TreeNode(4),
            TreeNode(7)
        )
    )
    q1 = TreeNode(5,
        TreeNode(3),
        TreeNode(6,
            TreeNode(4),
            TreeNode(7)
        )
    )
    print(is_same_tree(p1, q1))  # True

    # Пример 2
    p2 = TreeNode(1,
        TreeNode(2),
        None
    )
    q2 = TreeNode(1,
        None,
        TreeNode(2)
    )
    print(is_same_tree(p2, q2))  # False

    # Пример 3
    p3 = TreeNode(1,
        TreeNode(2),
        TreeNode(1)
    )
    q3 = TreeNode(1,
        TreeNode(1),
        TreeNode(2)
    )
    print(is_same_tree(p3, q3))  # False


# Оценка сложности:
# Время: O(n), где n — минимальное число узлов в двух деревьях (в худшем случае O(min(n_p, n_q)) ≈ O(n))
# Память: O(h), где h — высота дерева (глубина рекурсии)
