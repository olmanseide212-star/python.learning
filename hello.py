# Hello, World!")
# print("李常勇"print("你好，世界！")
# print(")
# print("你好")
# print("朋友")

# age = 18
# print(age)
# name = "遂川中学"   
# print(name)
# age = 18
# length = 180
# print(age)
# print(length)
# a = 10
# b = 2.5
# z = "10"
# print(a)
# print(b)
# print(z)
# print("花切")
# name = "李常勇"
# print("我的名字是：" + name)
# age = "18"
# print("我的年龄是：" + age)
# user_name = input("请输入你的名字：")
# print("你好，" + user_name)
# age_num = int(input("请输入你的年龄:"))

# next_age = age_num + 2
# print(next_age)
# print(10 //  3)
# print(10 % 3)
# print("2026年我要上清华大学")
# def price(o_price,multiplier):
#     result = o_price * multiplier
#     return result 
# o_price = float(input("请输入原价:"))
# multiplier = float(input("请输入折率:"))
# final_price = price(o_price, multiplier)
# print(f"请支付{final_price}元")

# hero = "孙悟空"
# attack = 150
# is_critical = True
# if is_critical == True:
#     damage = attack * 2
# else:
#     damage = attack
# print(f"{hero}发动暴击,输出了{damage}点暴击伤害")

# raw_winners = ["张三","李四","张三","王五","李四","赵六"]
# clean_winners = set(raw_winners)
# len(clean_winners)
# for w in clean_winners:
#     print(w)

def check_pass(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"
try:
    score = int(input("请输入宁的分数"))
    print(f"你的成绩判定为:{check_pass(score)}")
except:
    print("请输入纯数字")



