while True:

    a = float(input("计划月定投金额：")) #a: 每月定投金额
    n = int(input("计划投资年限：")) #n: 定投期数(公式中为n次方)
    x = float(input("预期年收益率：")) #x: 一年收益率

    m = x / 100 #注意收益率在这转化了

    M = 12 * a * (1 + m) * (-1 + (1 + m)**n) / m #M: 预期收益计算公式
    B = a*12*n
    H = M - B #净收益

    Y = H / B #
    
    print('————————————————————————————————————————————————')
    print("投资年限到期本金收益和：" + str(round(M,2)))
    print('到 期 后 的 本金 总额：' + str(round(B,2)))
    print("投资 年限 到期 总收益：" + str(round(H,2)))
    print("资产较本金增加的 比率：" + format(Y,'.2%'))
    print('  ')
    print('<><><><><><><><><><><><><><><><><><><><><><><><>')
    continue
