# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass


arr1 = [1,2,5,6]
target1 = 8

arr2 = [4,7,2, 6]
target2 = 12

def two_sum( nums:list[int], target:int) -> list[int]:
    for i in range (len (nums)):
        for j in range (i +1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

# answer=[]
answer = two_sum(arr1, target1)
print(answer)