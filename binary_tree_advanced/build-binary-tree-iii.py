"""
Массив из бинарного дерева

средне
решено

Дан корень бинарного дерева. Нужно представить бинарное дерево в виде массива по следующим правилам:

- Пусть result — массив, который нужно получить.
- Левый ребенок вершины в result[i] находится по индексу 2*i + 1.
- Правый ребенок — по индексу 2*i + 2.
- Если в дереве нет узла — в массиве ставим строку "null".
- Значение узла приводится к строке через str(node.val).
- В конце массива все лишние "null" (хвостовые) должны быть обрезаны.

ВАЖНО: используйте рекурсивную реализацию для сбора значений по индексам.

Пример 1:

Дерево: ["15","2","0","null","-1","null","6","null","null","5","8"]
Вывод: ["15","2","0","null","-1","null","6","null","null","5","8"]

Схема:
        15
       /  \
      2    0
       \    \
       -1   6
       / \
      5   8

Пример 2:

Дерево: ["-3"]
Вывод: ["-3"]

Схема:
   -3

Ограничения:
- Число узлов в дереве ≥ 1
- Высота дерева ≤ 1000
- Значения узлов в диапазоне [-10000, 10000]
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_array(root: Optional[TreeNode]) -> List[str]:
    """
    Преобразует бинарное дерево в массив строк с помощью рекурсии по индексам.
    """
    # словарь: индекс -> строковое значение
    mapping: dict[int, str] = {}

    def dfs(node: Optional[TreeNode], idx: int) -> None:
        if not node:
            return
        mapping[idx] = str(node.val)
        dfs(node.left, 2*idx + 1)
        dfs(node.right, 2*idx + 2)

    dfs(root, 0)
    if not mapping:
        return []
    max_idx = max(mapping)
    result = ["null"] * (max_idx + 1)
    for i, val in mapping.items():
        result[i] = val
    # убираем лишние "null" с конца
    while result and result[-1] == "null":
        result.pop()
    return result


# Примеры тестов
if __name__ == "__main__":
    # Пример 1
    # Строим дерево вручную:
    root1 = TreeNode(
        15,
        TreeNode(2,
            None,
            TreeNode(-1,
                TreeNode(5),
                TreeNode(8)
            )
        ),
        TreeNode(0,
            None,
            TreeNode(6)
        )
    )
    print(tree_to_array(root1))
    # → ["15","2","0","null","-1","null","6","null","null","5","8"]

    # Пример 2
    root2 = TreeNode(-3)
    print(tree_to_array(root2))  # → ["-3"]

# Оценка сложности:
# Время: O(n), где n — число узлов
# Память: O(n) для словаря и результата + O(h) стек рекурсии
