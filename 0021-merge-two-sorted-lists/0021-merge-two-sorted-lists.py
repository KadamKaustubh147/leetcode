# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = list1, list2
        
    
        dummy = ListNode()
        curr = dummy

        while p and q:
            if p.val <= q.val:
                print(f"{p.val} {q.val}")
                
                curr.next = p
                p = p.next
            elif p.val > q.val:
                print(f"{p.val} {q.val}")
                curr.next = q
                q = q.next
            
            # this was the most important step --> mistake i did
            curr = curr.next
        
        if p or q:
            curr.next = p or q
        
        return dummy.next