"""
Разворот

легко
решено

Дана голова односвязного списка head, нужно его развернуть,
не создавая новый список, и вернуть результат.

Пример 1:

Ввод: head = [1,2,3,4,5]
Вывод: [5,4,3,2,1]

Пример 2:

Ввод: head = [1,2,3]
Вывод: [3,2,1]

Пример 3:

Ввод: head = [1]
Вывод: [1]

Ограничения:

len(head) >= 0
"""

from typing import *

class ListNode:
    def __init__(self, val: int, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        res = []
        head = self
        while head:
            res.append(str(head.val))
            head = head.next

        return "->".join(res)

head1 = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4,
                                           ListNode(5)))))

head2 = ListNode(1,
                ListNode(2,
                         ListNode(3)))

head3 = ListNode(1)


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        # Сохраняем текущий узел
        tmp = curr
        # Переходим к следующему узлу
        curr = curr.next
        # Разворачиваем указатель
        tmp.next = prev
        # Обновляем предыдущий узел
        prev = tmp
    return prev


if __name__ == "__main__":
    ans1 = reverse_list(head1)
    ans2 = reverse_list(head2)
    ans3 = reverse_list(head3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Время: O(n), где n - число элементов в односвязном списке head
Память: O(1)
"""