# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(-600)
        dummy.next = head

        # Step 1: reach node before `left`
        q = dummy
        for _ in range(1,left):
            q = q.next

        # Step 2: reverse from left to right
        prev = None
        curr = q.next

        for _ in range(right - left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: reconnect
        tail = q.next          # old left node (now tail) --> last node of the reversed list in the exmaple it is 2 as 2 is last in the reversed case
        q.next = prev
        tail.next = curr

        # for i in range(3):
        #     print(i)

        return dummy.next
