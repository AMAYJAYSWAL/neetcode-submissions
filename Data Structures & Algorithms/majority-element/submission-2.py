class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for num in nums:
            if num not in a:
                a[num]=0
            a[num]+=1
            if a[num]>len(nums)//2:
                return num