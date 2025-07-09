#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write

if __name__ == "__main__":
    obj = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(obj.removeDuplicates(nums))
