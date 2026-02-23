class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = []
        nums2 = []

        for i in nums:
            nums1.append(i)
            nums2.append(i)

        return nums1 + nums2
