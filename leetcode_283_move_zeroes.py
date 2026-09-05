"""
LeetCode 283. 移动零 (Move Zeroes)

题目描述：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下 原地（in-place） 对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]

提示:
- 不能创建新的列表，必须直接修改传入的 nums。
"""

def move_zeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 在这里写下你的解法：
    insert_pos = 0
    for i in nums:
        if i != 0:
            nums[insert_pos] = i
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

        




# 测试代码
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [2, 1, 0, 3, 0]
    ]
    for test in test_cases:
        # 为了方便打印，我们把原始输入复制一份用来展示
        original = test.copy()
        move_zeroes(test)
        print(f"输入: {original} \t-> 结果: {test}")
