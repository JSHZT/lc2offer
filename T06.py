# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

        
if __name__ == "__main__":
    solution = Solution()
    result = solution()