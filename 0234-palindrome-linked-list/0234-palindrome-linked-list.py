# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # finding middle of linked list

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing the linked list from the middle element

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        # setting middle node's next to be None
        slow.next = None

        left = head

        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True



