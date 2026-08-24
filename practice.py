for i in range(1,31):
    if (i % 7 ==0):
        print("过")
    print(i)




def calc_price(price, is_vip):
    if is_vip == True:
        return price * 0.8
    else:
        return price
vip_price = calc_price(100,True)
print(f"vip用户的结账价格是：{vip_price}")
# 1. 纯计算大脑（负责打折算法）
def calc_price(price, is_vip):
    if is_vip:
        return price * 0.8
    else:
        return price

# 2. 前台接待员（负责询问并防呆）
try:
    # 步骤一：输入原价（用 float 支持带小数点的价格，如 99.5）
    price_input = float(input("请输入商品原价（元）："))
    
    # 步骤二：询问会员情况（输入 y 代表是，其他代表否）
    vip_input = input("请问您是 VIP 会员吗？(y/n)：")
    
    # 判断是否是 VIP（如果是 'y' 或者 'Y' 则为 True）
    is_vip = (vip_input.lower() == "y")
    
    # 步骤三：调用函数算账
    final_price = calc_price(price_input, is_vip)
    
    # 步骤四：打印最终账单
    print(f"🎉 结算完成！实际应付金额为：{final_price} 元")

except:
    print("⚠️ 价格输入不合法，请输入纯数字！")

