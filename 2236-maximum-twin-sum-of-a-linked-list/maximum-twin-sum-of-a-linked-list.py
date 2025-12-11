class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        maxVal = 0

        # Find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Compute maximum twin sum
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            head = head.next
            prev = prev.next

        return maxVal
