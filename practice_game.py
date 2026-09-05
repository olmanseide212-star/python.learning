heroes = {
    "zhan": {"name": "战士", "attack": 70, "hp": 200, "potions": 2},
    "fa": {"name": "法师", "attack": 90, "hp": 150, "potions": 4}
}

monsters = [
    {"name": "哥布林", "attack": 20, "hp": 50},
    {"name": "恶龙", "attack": 40, "hp": 100}
]

hero_choice = input("请选择你的英雄(zhan, fa): ").strip().lower()
if hero_choice not in heroes:
    print("输入有误，默认选择【战士】")
player = heroes.get(hero_choice, heroes["zhan"])

import random
boss = random.choice(monsters)

print(f"你遭遇了 {boss['name']} (血量: {boss['hp']}, 攻击力: {boss['attack']})")
while True:
    print("\n1:战斗", "2:使用药水", "3:逃跑")
    try:
        choice = input("请选择操作(1-3): ")
        if choice == "1":
            boss["hp"] -= player["attack"]
            print(f"你造成了 {player['attack']} 点伤害，boss剩余血量: {boss['hp']}")
            if boss["hp"] > 0:
                player["hp"] -= boss["attack"]
                print(f"boss反击了你，造成了 {boss['attack']} 点伤害，你的剩余血量: {player['hp']}")
                if player["hp"] <= 0:
                    print("你倒下了，游戏结束！")
                    break
            else:
                print("成功击败了 boss！")
                break
        elif choice == "2":
            if player["potions"] > 0:
                player["hp"] += 100
                player["potions"] -= 1
                print(f"使用药水成功！血量增加100 (当前血量: {player['hp']}, 剩余药水: {player['potions']}瓶)")
            else:
                print("药水已用尽，无法使用！")

        elif choice == "3":
            print("正在撤离战场...")
            break
        else:
            print("请输入正确的选项(1-3)")
    except Exception as e:
        print("发生错误：", e)