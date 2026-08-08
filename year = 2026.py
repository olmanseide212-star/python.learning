print("2026年我要上清华大学")
print(17 // 5)
print(17 % 5)
age = 17
if age >= 18:
    print("成年了，可以去网吧玩游戏了！")
else:
    print("回家写作业")
for K in range(3):
    print("我爱花切")
num = 1
while num <= 6:
    print("当前数字是:" + str(num))
    num = num + 1
for i in range(1, 11):
    if i == 7:
        continue
    print(i)
secret = 1234
while True:
    guess = int(input("请输入密码:"))
    if guess == secret:
        print("密码正确")
        break
    else:
        print("密码错误")
cart = ["书包"]