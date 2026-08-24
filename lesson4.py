# def multiply(x,y):
#     result = x * y
#     return result
# total = multiply(4,6)
# print(f"算出来的结果是：{total}")
# # import random
# import time
# print("正在启动幸运大转盘")
# time.sleep(2)
# prizes = ["一等奖:MacBook","二等奖:iPhone","三等奖:机械键盘"]
# lucky = random.choice(prizes)
# print(f"恭喜你抽中了:{lucky}")
# try:
#     num = int(input("请输入一个非零整数："))
#     print("100除以你的数字结果是:",100 / num)
# except:
#     print("发生错误!你可能输入了字母,或者输入了不能被除0")
with open("my_dteam.txt","w",encoding="utf-8") as f:
    f.write("李常勇的python档案：2026年考上侵华大学！\n")
print("硬盘文件创建成功")
with open("my_dteam.txt","r",encoding="utf-8") as f:
    text = f.read()
print("硬盘数据读取成功",text)

