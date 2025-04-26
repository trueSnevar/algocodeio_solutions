"""
Палиндром

средне
решено

Дана голова односвязного списка head.
Необходимо определить, является ли список палиндромом.
Если список является палиндромом, вернуть true, в противном случае — false.
Палиндромом считается тот список, который при развороте не изменяется.

Пример 1:

Ввод: head = [1,2,3,2,1]
Вывод: true

Пример 2:

Ввод: head = [1,2,3,4]
Вывод: false

Пример 3:

Ввод: head = [1]
Вывод: true

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
                                  ListNode(2,
                                           ListNode(1)))))

head2 = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4))))

head3 = ListNode(1)


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None
    while curr:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

def is_palindrome(head: Optional[ListNode]) -> bool:
    first_half_end = middle_node(head)
    second_half_begin = reverse_list(first_half_end)
    p1, p2 = head, second_half_begin
    while p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True


if __name__ == "__main__":
    ans1 = is_palindrome(head1)
    ans2 = is_palindrome(head2)
    ans3 = is_palindrome(head3)
    print(ans1)
    print(ans2)
    print(ans3)

"""
Время: O(n), где n - число элементов в односвязном списке head
Память: O(1)
"""