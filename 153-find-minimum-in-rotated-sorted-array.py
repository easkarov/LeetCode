class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, y = nums[0], nums[-1]

        if x <= y:
            return x

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m - 1] <= nums[m] <= nums[m + 1]:
                if nums[m] < y:
                    r = m - 1
                elif nums[m] > x:
                    l = m + 1
                continue

            return min(nums[m - 1], nums[m], nums[m + 1])

