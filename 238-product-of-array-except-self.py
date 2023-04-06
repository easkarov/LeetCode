class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1]
        suffix = [1]

        for k in nums:
            prefix.append(prefix[-1] * k)

        for i in range(n):
            suffix.append(suffix[-1] * nums[n - i - 1])
        suffix.reverse()

        return [prefix[i] * suffix[i + 1] for i in range(n)]