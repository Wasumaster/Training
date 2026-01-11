# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        str1 = ""
        str2 = ""
        sumcomb = 0
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        current = dummy
        while p1 is not None:
            str1 += str(p1.val)
            p1 = p1.next

        while p2 is not None:
            str2 += str(p2.val)
            p2 = p2.next 

        str1 = str1[::-1]
        str2 = str2[::-1]
        sum1 = int(str1)
        sum2 = int(str2)
        sumcomb = sum1 + sum2
        if sumcomb == 0:
            return dummy
        while sumcomb > 0:
            val = sumcomb % 10
            current.next = ListNode(val)
            current = current.next
            sumcomb = sumcomb // 10 
        return dummy.next
        

    