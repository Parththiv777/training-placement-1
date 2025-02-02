# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d = ListNode()
        cur = d
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                cur = list2
                list2 = list2.next
                
            else :
                cur.next = list1
                cur = list1
                list1 = list1.next
                
        cur.next = list1 if list1 else list2      
        return d.next         
        
