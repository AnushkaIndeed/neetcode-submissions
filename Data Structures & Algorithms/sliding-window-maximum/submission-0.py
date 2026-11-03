from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        result = []

        for i in range(len(nums)):

            # Remove indices outside the current window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add current index
            q.append(i)

            # Record maximum once window reaches size k
            if i >= k - 1:
                result.append(nums[q[0]])

        return result
