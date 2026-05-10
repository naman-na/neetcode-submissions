class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = set()
        #for i,j in enumerate(nums):

            #print(i,j)
           
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    out.add(i)
                    out.add(j)
        return list(out)
