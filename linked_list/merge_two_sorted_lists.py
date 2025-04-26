"""
Слияние

легко
решено

Даны головы двух отсортированных по возрастанию односвязных списков head1 и head2.
Необходимо объединить эти два списка в один отсортированный список.
Новый список должен быть создан путем объединения узлов из первых двух списков.
Вернуть голову объединенного отсортированного списка.

Пример 1:

Ввод: head1 = [1,3,5], head2 = [2,4,6]
Вывод: [1,2,3,4,5,6]

Пример 2:

Ввод: head1 = [1,2,3], head2 = []
Вывод: [1,2,3]

Пример 3:

Ввод: head1 = [], head2 = []
Вывод: []
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
                ListNode(3,
                         ListNode(5)))


head2 = ListNode(2,
                ListNode(4,
                         ListNode(6)))

head3 = ListNode(1,
                ListNode(2,
                         ListNode(3)))


head4 = None


def get_val(node: ListNode):
    if node is None:
        return float('inf')
    return node.val

def merge_two_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
    curr = dummy = ListNode(0)
    while head1 is not None or head2 is not None:
        if get_val(head1) < get_val(head2):
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    ans1 = merge_two_lists(head1, head2)
    ans2 = merge_two_lists(head3, head4)
    print(ans1)
    print(ans2)


"""
Время: O(n), где n - число элементов в односвязном списке head
Память: O(1)
"""