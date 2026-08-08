target = 12
count = 0
print("欢迎来到猜数字游戏,我想了一个1到100的整数,你来猜")
while True:
    guess = int(input("请输入你猜的数字"))
    count = count + 1
    if guess > target:
        print("哎呀，太大了")
    elif guess < target:
        print("太小了,再往大点猜")
    else:
        print("你猜对了")
        print("你一共尝试了" + str(count) + "次")
        break

