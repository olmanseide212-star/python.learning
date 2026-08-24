"""
Day 2: 对撞双指针（首尾向中间夹逼）
题目 1: LeetCode 125. 验证回文串 (Valid Palindrome)
"""

def is_palindrome(s: str) -> bool:
    # 步骤 1：清洗数据（只保留字母和数字，并统一转为小写）
    # isalnum: is alpha-numeric (是否为字母或数字)
    # lower: 转小写
    clean_s = "".join(ch.lower() for ch in s if ch.isalnum())
    
    # 步骤 2：对撞双指针
    left = 0
    right = len(clean_s) - 1
    
    while left < right:
        if clean_s[left] != clean_s[right]:
            return False  # 一旦发现不对称，立刻返回 False
        
        # 对称匹配成功，两边向中间靠拢
        left += 1
        right -= 1
        
    return True  # 全部比对完成，是对称的


if __name__ == "__main__":
    # 测试用例 1
    test1 = "racecar"
    print(f"用例 1 ('{test1}') 结果: {is_palindrome(test1)}")  # 期望: True

    # 测试用例 2
    test2 = "hello"
    print(f"用例 2 ('{test2}') 结果: {is_palindrome(test2)}")  # 期望: False

    # 测试用例 3
    test3 = "A man, a plan, a canal: Panama"
    print(f"用例 3 ('{test3}') 结果: {is_palindrome(test3)}")  # 期望: True
