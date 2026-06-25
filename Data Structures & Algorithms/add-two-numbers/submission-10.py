class Solution:
    def addTwoNumbers(self, l1, l2):

        str1 = ""
        curr = l1
        while curr:
            str1 += str(curr.val)
            curr = curr.next

        str2 = ""
        curr = l2
        while curr:
            str2 += str(curr.val)
            curr = curr.next

        num1 = int(str1[::-1])
        num2 = int(str2[::-1])

        x = str(num1 + num2)

        dummy = ListNode()
        node = dummy

        for digit in x[::-1]:
            node.next = ListNode(int(digit))
            node = node.next

        return dummy.next