# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1.reverse()
        l2.reverse()
        x = int(''.join(map(str, l1)))
        y = int(''.join(map(str, l2)))
        sum = x + y
        BeReverseList = list(str(sum))
        BeReverseList.reverse()
        return BeReverseList
