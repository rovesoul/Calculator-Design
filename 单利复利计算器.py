while True:
    print('单利计算VS 复利同时出')
    p= float(input('输入你的本金'))
    i=float(input('输入年利率'))
    k=int(input('存几年？'))
    for j in range(1,k+1):
        # Timelong=float(i)
        # Timelong=float(input('输入存几年'))
        print('第'+ str(j)+'年-----------------------------')
        danf=p+p*i*j#单利本金及利息
        fuf=p *((1.00+i) ** j )#复利本金及利息
        beilv=round(fuf/danf,2)
        fubei=round(fuf/p,2)
        print('单利利息是 %.2f'% danf)
        print('复利利息是 %.2f'% fuf)
        print('复/单倍数'+ str(beilv))
        print('复利/本金倍数'+ str(fubei))
    continueme=input('继续嘛？n停止其他继续')
    if continueme=='n':
        break
    else:
        continue
