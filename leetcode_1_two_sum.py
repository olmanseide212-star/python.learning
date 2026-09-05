"""
LeetCode 1. 两数之和 (Two Sum)

题目描述：
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的下标。

示例：
nums = [2, 7, 11, 15], target = 9
输出: [0, 1]  (因为 nums[0] + nums[1] == 2 + 7 == 9)
"""

def two_sum(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]
        else:
            seen[num] = i



# 测试代码
if __name__ == "__main__":
    test_nums = [2, 7, 11, 15]
    test_target = 9
    result = two_sum(test_nums, test_target)
    print(f"输入: nums = {test_nums}, target = {test_target}")
    print(f"结果下标: {result}")
    print(f"对应的数字: [{test_nums[result[0]]}, {test_nums[result[1]]}]")
