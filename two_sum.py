# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         pass


arr1 = [1,2,5,6]
target1 = 8

arr2 = [4,7,2, 6]
target2 = 12

def two_sum( nums, target) : 
    for i in range (len (nums)):

        for j in range (i +1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]
    return []

answer = two_sum(arr1, target1)
print(answer)

answer = two_sum(arr2, target2)
print(answer)



complementaryMap = dict()


def f1(lis, targ):
    for i in range (len(lis)):
        complement = targ -lis[i]
        num = lis[i]
        if num in complementaryMap:
            return [complementaryMap[num],i]
        else:
            complementaryMap[complement] = i

cm = f1([1,2,5,6,8,9],10)
print(cm)


