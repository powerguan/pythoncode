"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

numbers = [2,11,7]
target = 9

for i in range(0, len(numbers)-1):
    for k in range(i+1, len(numbers)):
        if (numbers[i] + numbers[k] == target):
            print(f"find them: {i}, {k}")


"""
从数组里找出和为target的两个数
"""
numbers = [8, 10 ,11, 1,  7, 3, 13, 19]
target = 17
# first: sort list
numbers.sort()


left = 0
right = len(numbers) - 1
while left < right:
    leftValue = numbers[left]
    rightValue = numbers[right]
    if leftValue + rightValue == target:
        print(f"find them: {leftValue} + {rightValue} = {target}")
        break
    elif leftValue + rightValue > target:
        right = right -1
    elif leftValue + rightValue < target:
        left = left + 1



