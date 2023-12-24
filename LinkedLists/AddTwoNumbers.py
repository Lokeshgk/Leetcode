# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        excess = 0
        while l1 is not None or l2 is not None:
            a = 0
            b = 0
            if l1 is not None:
                a = l1.val
            if l2 is not None:
                b = l2.val
            
            # Find SUM
            s = a + b
            #print(sum)
            s = s + excess

            if s >= 10:
                excess = 1
                res = s % 10
            else:
                res = s
                excess = 0
            
            print(res)
            node = ListNode(res)

            if result is None:
                result = node
            else:
                temp = result
                while temp.next is not None:
                    temp = temp.next
                temp.next = node
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if excess != 0:
            node = ListNode(excess)
        
            if result is None:
                result = node
            else:
                temp = result
                while temp.next is not None:
                    temp = temp.next
                temp.next = node

        return result

        