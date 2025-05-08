"""
Наименьший общий предок (LCA) с учётом отсутствующих узлов

средне
решено

Дан корень бинарного дерева и два значения p_val, q_val, которые могут как присутствовать в дереве, так и отсутствовать.
Нужно вернуть узел, являющийся наименьшим общим предком (LCA) этих двух значений, или None, если один (или оба)
значения отсутствуют в дереве.

LCA — это узел, потомками которого (включая сам узел) являются оба узла p и q, и у которого нет более глубокого
узла с этим свойством.

ВАЖНО: реализовать рекурсивный обход.

Пример 1:

Ввод: root = [1,2,0,3,-1,null,6,null,null,5,8,null,12], p = 2, q = 8
Вывод: 2

Схема дерева:
             1
           /   \
          2     0
         / \     \
        3  -1     6
           / \     \
          5   8     12

— узел с val=2 является LCA для p=2 и q=8 (при этом p является предком q).

Пример 2:

Ввод: root = [1,2,0,3,-1,null,6,null,null,5,8,null,12], p = 6, q = 14
Вывод: None

Схема: то же дерево, но значение 14 отсутствует в дереве → LCA не определён.

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значения узлов в диапазоне [-10000, 10000]
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
    Находит LCA узлов со значениями p_val и q_val в дереве или возвращает None,
    если хотя бы одно значение отсутствует.
    """
    # Рекурсивно ищем кандидата для LCA без проверки существования обоих
    def find(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        left = find(node.left)
        right = find(node.right)
        if node.val == p_val or node.val == q_val:
            return node
        if left and right:
            return node
        return left or right

    # Проверка существования значения в дереве
    def exists(node: Optional[TreeNode], target: int) -> bool:
        if not node:
            return False
        if node.val == target:
            return True
        return exists(node.left, target) or exists(node.right, target)

    lca = find(root)
    # Убедимся, что оба присутствуют и LCA действительно содержит их
    if lca and exists(root, p_val) and exists(root, q_val):
        return lca
    return None


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
    lca1 = lowest_common_ancestor(root, 2, 8)
    print(lca1.val if lca1 else None)  # 2

    # Пример 2
    lca2 = lowest_common_ancestor(root, 6, 14)
    print(lca2.val if lca2 else None)  # None

# Оценка сложности:
# Время: O(n), где n — число узлов (два обхода: find + exists для каждого)
# Память: O(h), где h — высота дерева (рекурсивный стек)
