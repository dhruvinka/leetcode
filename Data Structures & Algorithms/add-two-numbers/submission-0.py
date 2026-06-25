# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1=""
        curr=l1
        while curr:
            str1+=curr.val
            curr=curr.next

        str2=""
        cur2=l1
        while curr2:
            str2+=curr2.val
            curr2=curr2.next
        print(str1+str2)
        