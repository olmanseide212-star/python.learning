students = []
while True:
    print("=="*30)
    print("班级成绩管理系统")
    print("=="*30)
    print("1:添加学生成绩")
    print("2:查看班级成绩")
    print("3:统计班级平均")
    print("4:退出并保存")

    choice = input("请选择操作(1-4):")

    if choice == "1":
        name = input("请输入你的姓名：")
        score = float(input("请输入你的成绩："))
        stu = {"name":name,"score":score}
        students.append(stu)
        print(f"成功转入{name}的成绩：{score}分")
    if choice == "2":
        if len(students) == 0:
            print("还没有录入任何成绩")
        else:
            for s in students:
                print(f"姓名：{s['name']}成绩:{s['score']}分")
    if choice == "3":
        print("全班成绩统计")
        if len(students) == 0:
            print("还没有录入任何成绩，无法统计")
        else:
            total_score = 0
            for s in students:
                total_score += s["score"]
            avg = total_score / len(students)
            print(f"全班总人数：{len(students)}人")
            print(f"全班总分:{total_score}分")
            print(f"全班平均分：{avg}分")
    if choice == "4":
        with open("class_scores.txt","w",encoding="utf-8") as f:
            f.write("===2026年 班级成绩总单 ===\n")
            for s in students:
                f.write(f"姓名:{s['name']}|成绩:{s['score']}分\n")
        print("全班成绩已保存")
        print("正在退出系统再见")
        break