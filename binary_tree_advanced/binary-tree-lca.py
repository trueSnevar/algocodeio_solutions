"""
НОП не нулевых вершин (Lowest Common Ancestor)

средне
решено

Дан корень бинарного дерева и две вершины, которые гарантированно присутствуют в дереве.
Нужно вернуть для двух вершин наименьшего общего предка (НОП).

НОП — это узел, потомками которого являются узлы p и q, при этом НОП может быть только единственным
и имеет наименьшее расстояние от p, q. Учти, что узел может быть потомком самого себя
(см. пример 2).

ВАЖНО: реализуй обход с использованием рекурсии

Пример 1:

Ввод: root = [1,2,0,3,-1,null,6,null,null,5,8,null,12], p = -1, q = 12
Вывод: 1

Схема:
             1
           /   \
          2     0
         / \     \
        3  -1     6
           / \     \
          5   8     12

Пример 2:

Ввод: root = [1,2,0,3,-1,null,6,null,null,5,8,null,12], p = 2, q = 8
Вывод: 2

Схема (то же дерево):
             1
           /   \
          2     0
         / \     \
        3  -1     6
           / \     \
          5   8     12

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значение вершин в диапазоне [-10000, 10000]
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode],
                             p_val: int,
                             q_val: int) -> Optional[TreeNode]:
    """
    Находит НОП двух узлов по их значениям в бинарном дереве.
    Возвращает сам узел-предок или None, если дерево пусто.
    """
    if not root:
        return None
    # Если текущий узел — один из искомых, возвращаем его
    if root.val == p_val or root.val == q_val:
        return root
    # Ищем в левом и правом поддеревьях
    left = lowest_common_ancestor(root.left, p_val, q_val)
    right = lowest_common_ancestor(root.right, p_val, q_val)
    # Если оба оказались ненулевыми — текущий узел и есть НОП
    if left and right:
        return root
    # Иначе один из них или ни одного
    return left or right


if __name__ == "__main__":
    # Строим дерево для примеров
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3),
            TreeNode(-1,
                TreeNode(5),
                TreeNode(8)
            )
        ),
        TreeNode(
            0,
            None,
            TreeNode(6,
                None,
                TreeNode(12)
            )
        )
    )
    # Пример 1
    lca1 = lowest_common_ancestor(root, -1, 12)
    print(lca1.val if lca1 else None)  # 1

    # Пример 2
    lca2 = lowest_common_ancestor(root, 2, 8)
    print(lca2.val if lca2 else None)  # 2

# Оценка сложности:
# Время: O(n), где n — число узлов в дереве
# Память: O(h), где h — высота дерева (стек рекурсии)
