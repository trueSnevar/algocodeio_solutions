"""
Бинарное дерево из массива

средне
решено

Дан массив строк tree, где tree[i] может быть как целым числом, представленным строкой,
так и "null". Нужно преобразовать этот массив в бинарное дерево по правилам:

- tree[0] – корень бинарного дерева
- Левый ребенок вершины tree[i] – tree[2*i+1]
- Правый ребенок вершины tree[i] – tree[2*i+2]
- Если tree[i] == "null" или i >= len(tree), считается, что узла нет (None)
- Иначе tree[i] конвертируется в int для значения узла

ВАЖНО: используй рекурсивную реализацию

Пример 1:

Ввод: tree = ["15","2","0","null","-1","null","6","null","null","5","8"]
Вывод: [15,2,0,null,-1,null,6,null,null,5,8]

Схема:
        15
       /  \
      2    0
       \    \
       -1   6
       / \
      5   8

Пример 2:

Ввод: tree = ["-3"]
Вывод: [-3]

Схема:
  -3

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значения узлов в диапазоне [-10000, 10000]
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree(tree: List[str]) -> Optional[TreeNode]:
    """
    Рекурсивно строит дерево из массива строк.
    """
    def build(idx: int) -> Optional[TreeNode]:
        if idx >= len(tree) or tree[idx] == 'null':
            return None
        node = TreeNode(int(tree[idx]))
        node.left = build(2*idx + 1)
        node.right = build(2*idx + 2)
        return node

    return build(0)


def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Сериализует дерево в массив в level-order, убирая хвостовые None.
    """
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # обрезаем хвостовые None
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    # Пример 1
    tree1 = ["15","2","0","null","-1","null","6","null","null","5","8"]
    root1 = build_binary_tree(tree1)
    print(serialize_tree(root1))  # [15, 2, 0, None, -1, None, 6, None, None, 5, 8]

    # Пример 2
    tree2 = ["-3"]
    root2 = build_binary_tree(tree2)
    print(serialize_tree(root2))  # [-3]

# Оценка сложности:
# Время: O(n), где n — длина массива tree
# Память: O(h) стек рекурсии, где h — высота дерева
