"""
LeetCode 20. 有效的括号 (Valid Parentheses)

题目描述：
给定一个只包括 '(', ')', '{', '}', '[', ']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例：
s = "()"        -> True
s = "()[]{}"    -> True
s = "(]"        -> False
s = "([)]"      -> False
"""

def is_valid(s: str) -> bool:
    # 配对字典：右括号 -> 对应的左括号
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    stack = []  # 用列表当作“栈”
    # 在这里写下你的解法：
    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop() 
        else:
            stack.append(char)           
    return len(stack) == 0



# 测试代码
if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in test_cases:
        result = is_valid(test)
        print(f"输入: '{test}' \t-> 结果: {result}")
