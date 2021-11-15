#
# Description here: https://leetcode.com/problems/add-two-numbers/
# faster than 5% of python3 submissions
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p=0
        i1=0
        i2=0
        result=ListNode(0)
        print(result)
        print(result.next )
        while l1 != None:
            i1=i1+l1.val*(10**p)
            p=p+1
            l1=l1.next
        print(i1)
        p=0
        while l2 != None:
            i2=i2+l2.val*(10**p)
            p=p+1
            l2=l2.next
        print(i2)
        sum=i1+i2
        result=ListNode(sum % 10)
        sum = sum // 10
        result_tail = result
        while (sum != 0):
            print ("sum is {0} adding {1}".format(sum, (sum %10)))
            result_tail.next = ListNode(sum % 10)
            result_tail = result_tail.next
            sum = sum // 10
            print ("result is {0}".format(result))
        return result
            
