"""
Поиск середины

легко
решено

Дана голова односвязного списка head. Необходимо найти значение среднего узла этого списка и вернуть его.
Если в списке нечётное количество узлов, вернуть единственное значение среднего узла.
Если в списке четное количество узлов, вернуть значение второго из двух средних узлов.

Пример 1:

Ввод: head = [1,2,3,4,5]
Вывод: 3
Объяснение: Средний узел списка это узел 3.

Пример 2:

Ввод: head = [1,2,3,4]
Вывод: 3
Объяснение: У списка два средних узла 2 и 3, но по условию задачи надо взять второй.

Пример 3:

Ввод: head = [1]
Вывод: 1
Ограничения:

len(head) >= 0
"""

from typing import *

class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next

head1 = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4,
                                           ListNode(5)))))

head2 = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4))))

head3 = ListNode(1)


def middle_node_value(head: ListNode) -> int:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


if __name__ == "__main__":
    ans1 = middle_node_value(head1)
    ans2 = middle_node_value(head2)
    ans3 = middle_node_value(head3)
    print(ans1)
    print(ans2)
    print(ans3)


"""
Время: O(n), где n - число элементов в односвязном списке head
Память: O(1)
"""