class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lis=[0]*(n*2)
        for i in range(n):
            lis[i]=lis[i+n]=nums[i]
        return lis