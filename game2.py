import random
def draw_one():
    luck = random.randint(1,100)
    if luck <=5:
        card = "5"
    elif luck <= 25:
        card = "4"
    else:
        card = "3"
    return card
for i in range(10):
    result = draw_one()
    print(f"第{i+1}抽结果：{result}")
    import random
import time

# ==========================================
# 1. 游戏基础数据与卡池配置
# ==========================================
primogems = 1600   # 初始原石（够一次十连抽！）
pity_count = 0     # 保底计数器（距离上次出金抽了多少次）
bag = []           # 玩家背包（存储抽到的所有卡片）

# 豪华卡池定义
gold_cards = ["🌟【雷电将军】", "🌟【钟离】", "🌟【纳西妲】", "🌟【齐天大圣】"]
purple_cards = ["💜【班尼特】", "💜【行秋】", "💜【香菱】", "💜【铠】"]
blue_cards = ["💙【黎明神剑】", "💙【黑缨枪】", "💙【以理服人】", "💙【普通铁剑】"]

# ==========================================
# 2. 核心抽卡后端函数（带50抽大保底机制！）
# ==========================================
def draw_one():
    global pity_count  # 声明修改全局保底计数器
    pity_count += 1
    
    luck = random.randint(1, 100)
    
    # 触发 5% 概率 或 触发 50 抽大保底！
    if luck <= 5 or pity_count >= 50:
        card = random.choice(gold_cards)
        pity_count = 0  # 抽中金卡，保底重置归零！
    elif luck <= 25:
        card = random.choice(purple_cards)
    else:
        card = random.choice(blue_cards)
        
    bag.append(card)  # 自动存入玩家背包
    return card

# ==========================================
# 3. 游戏主菜单与交互主循环
# ==========================================
print("✨" * 25)
print("     🎮 欢迎来到【原石祈愿·抽卡模拟器】v1.0")
print("✨" * 25)

while True:
    print("\n" + "=" * 35)
    print(f"💎 当前原石余额：{primogems}  |  🎯 距离大保底还差：{50 - pity_count} 抽")
    print("=" * 35)
    print("1. 单抽一次 (消耗 160 原石)")
    print("2. 爽快十连抽 (消耗 1600 原石)")
    print("3. 查看我的背包与战绩")
    print("4. 免费领取原石福利 (+1600 原石)")
    print("5. 保存背包到硬盘并退出游戏")
    print("=" * 35)
    
    choice = input("👉 请选择你的操作 (1-5)：")
    
    # 功能 1：单抽
    if choice == "1":
        if primogems < 160:
            print("❌ 原石不足！请先去选项 4 领取免费原石！")
        else:
            primogems -= 160
            print("\n💫 祈愿流星划过天空...")
            time.sleep(0.8)
            result = draw_one()
            print(f"🎉 获得：{result}")
            
    # 功能 2：十连抽（for 循环连发 + 仪式感延时）
    elif choice == "2":
        if primogems < 1600:
            print("❌ 原石不足 1600！请先去选项 4 领取免费原石！")
        else:
            primogems -= 1600
            print("\n🌟🌟 十连抽启动！满屏金光正在汇聚...")
            print("-" * 35)
            for i in range(10):
                time.sleep(0.3)  # 每张卡停顿 0.3 秒，模拟开箱刺激感
                result = draw_one()
                print(f"第 {i+1} 抽 ➔ {result}")
            print("-" * 35)
            
    # 功能 3：查看背包
    elif choice == "3":
        print(f"\n🎒 【我的背包】(共累计抽卡 {len(bag)} 次)：")
        if len(bag) == 0:
            print("背包空空如也，快去抽卡吧！")
        else:
            # 统计金卡数量
            gold_num = 0
            for item in bag:
                if "🌟" in item:
                    gold_num += 1
            print(f"🏆 你一共斩获了 {gold_num} 张五星金色传说！")
            print("最新抽到的 5 件物品：", bag[-5:])
            
    # 功能 4：充值/领取原石
    elif choice == "4":
        primogems += 1600
        print("🎁 恭喜！已为你补充 1600 颗原石，又可以十连抽啦！")
        
    # 功能 5：存盘并退出
    elif choice == "5":
        with open("gacha_bag.txt", "w", encoding="utf-8") as f:
            f.write("=== 我的抽卡战绩总榜 ===\n")
            for item in bag:
                f.write(item + "\n")
        print("💾 背包战绩已成功永久保存到硬盘文件【gacha_bag.txt】！")
        print("👋 感谢游玩，祝你欧气满满，下次再见！")
        break
        
    else:
        print("⚠️ 输入无效，请输入数字 1 到 5！")
