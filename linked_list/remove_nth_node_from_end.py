"""
Удаление с конца

средне
решено

Дана голова односвязного списка head.
Необходимо удалить n-й узел с конца списка и вернуть голову измененного списка.

Пример 1:

Ввод: head = [1,2,3,4], n = 2
Вывод: [1,2,4]

Пример 2:

Ввод: head = [1,2,3], n = 3
Вывод: [2,3]

Пример 3:

Ввод: head = [1], n = 1
Вывод: []

Ограничения:

1 <= n <= len(head)
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
                                  ListNode(4))))

head2 = ListNode(1,
                ListNode(2,
                         ListNode(3)))

head3 = ListNode(1)


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummyNode = ListNode(val=0, next=head)

    fast = dummyNode
    for i in range(n + 1):
        fast = fast.next

    slow = dummyNode
    while fast is not None:
        slow = slow.next
        fast = fast.next

    # удаляем вершину
    slow.next = slow.next.next

    return dummyNode.next


if __name__ == "__main__":
    ans1 = remove_nth_from_end(head1, 2)
    ans2 = remove_nth_from_end(head2, 3)
    ans3 = remove_nth_from_end(head3, 1)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Время: O(n), где n - число элементов в односвязном списке head
Память: O(1)
"""