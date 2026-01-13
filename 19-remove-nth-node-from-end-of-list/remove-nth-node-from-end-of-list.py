# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)

        cur = head
        count = 0

        while cur:
            count += 1
            cur = cur.next
        cur = dummy
        element_number = count - n

        while element_number >0:
            
            cur = cur.next
            element_number -= 1

        if cur.next:
            cur.next = cur.next.next
        
        return dummy.next