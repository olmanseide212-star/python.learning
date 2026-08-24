"""
LeetCode 1. 两数之和 (Two Sum)
性能大比拼：暴力法 vs 哈希表法
"""
import time

# 方法一：暴力枚举法 O(n^2)
def two_sum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# 方法二：哈希表字典法 O(n)
def two_sum_hash(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    # 构造一个包含 10,000 个数字的大列表
    # 故意把答案放在最末尾：第 9998 个数(100) 和 第 9999 个数(200)，目标 target = 300
    big_nums = [1] * 10000
    big_nums[9998] = 100
    big_nums[9999] = 200
    target = 300

    print("📊 正在测试 10,000 个数据规模下的运行耗时...\n")

    # 1. 测试暴力法耗时
    start_time = time.time()
    res1 = two_sum(big_nums, target)
    cost1 = time.time() - start_time
    print(f"🐢 暴力法 (双重循环) 耗时: {cost1:.4f} 秒 | 结果: {res1}")

    # 2. 测试哈希表法耗时
    start_time = time.time()
    res2 = two_sum_hash(big_nums, target)
    cost2 = time.time() - start_time
    print(f"⚡ 哈希表 (字典法)   耗时: {cost2:.6f} 秒 | 结果: {res2}")

    print(f"\n🚀 哈希表法比暴力法快了大约 {cost1 / cost2:.0f} 倍！")
