# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None

        current_node = head
        count = 1

        while current_node.next:
            count += 1
            current_node = current_node.next

        k = k % count
        if k == 0 or count == 1:
            return head

        current_node.next = head

        steps_to_new_tail = count - k

        while steps_to_new_tail > 0:
            current_node = current_node.next
            steps_to_new_tail -= 1

        new_head = current_node.next
        current_node.next = None

        return new_head 