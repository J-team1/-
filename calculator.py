import tkinter #导入tkinter模块
import easygui
import relation
from decimal import Decimal,localcontext
import math
import numpy as np #导入np模块
with localcontext() as ctx:
    ctx.prec = 4
################################################################################################################################徐凯成
root = tkinter.Tk()
root.minsize(280,450)
root.maxsize(280,450)
root.title('百宝箱计算器')#显示标题
a=0
#界面布局
#显示面板
result = tkinter.StringVar()
result.set(0)#显示面板显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()#显示面板显示结果2，用于显示计算过程
result2.set('')
#显示版
label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
label.place(y=0,width = 280,height = 60)
label2 = tkinter.Label(root,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
label2.place(y = 60,width = 280,height = 60)

#数字键按钮
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('7'))
btn7.place(x = 0,y = 175,width = 70,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('8'))
btn8.place(x = 70,y = 175,width = 70,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('9'))
btn9.place(x = 140,y = 175,width = 70,height = 55)

btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('4'))
btn4.place(x = 0,y = 230,width = 70,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('5'))
btn5.place(x = 70,y = 230,width = 70,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('6'))
btn6.place(x = 140,y = 230,width = 70,height = 55)

btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('1'))
btn1.place(x = 0,y = 285,width = 70,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('2'))
btn2.place(x = 70,y = 285,width = 70,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('3'))
btn3.place(x = 140,y = 285,width = 70,height = 55)
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('0'))
btn0.place(x = 70,y = 340,width = 70,height = 55)


#运算符号按钮
#开始界面运算符
btnac = tkinter.Button(root,text = 'AC',bd = 0.5,font = ('黑体',20),fg = 'orange',command = lambda :pressCompute('AC'))
btnac.place(x = 0,y = 120,width = 70,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('b'))
btnback.place(x = 70,y = 120,width = 70,height = 55)
btna = tkinter.Button(root,text = '÷',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('/'))
btna.place(x = 140,y = 120,width = 70,height = 55)
btnb = tkinter.Button(root,text ='×',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda:pressCompute('*'))
btnb.place(x = 210,y = 120,width = 70,height = 55)
btnc = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('-'))
btnc.place(x = 210,y = 175,width = 70,height = 55)
btnd = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('+'))
btnd.place(x = 210,y = 230,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressEqual())
btnequ.place(x = 210,y = 285,width = 70,height = 110)
btne = tkinter.Button(root,text = '%',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('%'))
btne.place(x = 0,y = 340,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('.'))
btnpoint.place(x = 140,y = 340,width = 70,height = 55)
btne = tkinter.Button(root,text = 'sin',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:sin())
btne.place(x = 0,y = 395,width = 70,height = 55)
btne = tkinter.Button(root,text = 'cos',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:cos())
btne.place(x = 70,y = 395,width = 70,height = 55)
btne = tkinter.Button(root,text = 'tan',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:tan())
btne.place(x = 140,y = 395,width = 70,height = 55)
btne = tkinter.Button(root,text = 'ln',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:ln())
btne.place(x = 210,y = 395,width = 70,height = 55)
#各模式运算符切换
def pressModel(model):
    if model == '返回':
        btnac = tkinter.Button(root,text = 'AC',bd = 0.5,font = ('黑体',20),fg = 'orange',command = lambda :pressCompute('AC'))
        btnac.place(x = 0,y = 120,width = 70,height = 55)
        btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('b'))
        btnback.place(x = 70,y = 120,width = 70,height = 55)
        btna = tkinter.Button(root,text = '÷',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('/'))
        btna.place(x = 140,y = 120,width = 70,height = 55)
        btnb = tkinter.Button(root,text ='×',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda:pressCompute('*'))
        btnb.place(x = 210,y = 120,width = 70,height = 55)
        btnc = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('-'))
        btnc.place(x = 210,y = 175,width = 70,height = 55)
        btnd = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('+'))
        btnd.place(x = 210,y = 230,width = 70,height = 55)
        btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressEqual())
        btnequ.place(x = 210,y = 285,width = 70,height = 110)
        btne = tkinter.Button(root,text = '%',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('%'))
        btne.place(x = 0,y = 340,width = 70,height = 55)
        btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:pressCompute('.'))
        btnpoint.place(x = 140,y = 340,width = 70,height = 55)
    if model == '单位换算':
        btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('b'))
        btnback.place(x = 210,y = 175,width = 70,height = 110) 
        btna = tkinter.Button(root,text = '℃->℉',bd = 0.5,font = ('微软雅黑',15),fg = '#4F4F4F',command = lambda :pressCompute('*9/5+32'))
        btna.place(x = 0,y = 120,width = 93,height = 27.5)
        btnb = tkinter.Button(root,text = '℉->℃',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('/1.8-32/1.8'))
        btnb.place(x = 0,y = 147.5,width = 93,height = 27.5)
        btnc = tkinter.Button(root,text = 'm/s->km/h',font = ('微软雅黑',10),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('*3.6'))
        btnc.place(x = 93,y = 120,width = 93,height = 27.5)
        btnd = tkinter.Button(root,text = 'km/h->m/s',font = ('微软雅黑',10),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('/3.6'))
        btnd.place(x = 93,y = 147.5,width = 93,height = 27.5)
        btne = tkinter.Button(root,text = 'inch->cm',font = ('微软雅黑',10),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('*2.54'))
        btne.place(x = 186,y = 120,width = 94,height = 27.5)
        btnf = tkinter.Button(root,text = 'cm->inch',font = ('微软雅黑',10),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('/2.54'))
        btnf.place(x = 186,y = 147.5,width = 94,height = 27.5)       
        btnac = tkinter.Button(root,text = 'AC',font = ('微软雅黑',20),fg = 'orange',bd = 0.5,command = lambda:pressCompute('AC'))
        btnac.place(x = 0,y = 340,width = 70,height = 55)
    if model == '进制换算':
        btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressCompute('b'))
        btnback.place(x = 210,y = 175,width = 70,height = 220) 
        btna = tkinter.Button(root,text = '10->2',bd = 0.5,font = ('微软雅黑',15),fg = '#4F4F4F',command = lambda:bin102())
        btna.place(x = 0,y = 120,width = 93,height = 27.5)
        btnb = tkinter.Button(root,text = '2->10',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:int210())
        btnb.place(x = 0,y = 147.5,width = 93,height = 27.5)
        btnc = tkinter.Button(root,text = '2->8',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:oct28())
        btnc.place(x = 93,y = 120,width = 93,height = 27.5)
        btnd = tkinter.Button(root,text = '8->2',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:bin82())
        btnd.place(x = 93,y = 147.5,width = 93,height = 27.5)
        btne = tkinter.Button(root,text = '10->8',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:oct108())
        btne.place(x = 186,y = 120,width = 94,height = 27.5)
        btnf = tkinter.Button(root,text = '8->10',font = ('微软雅黑',15),fg = '#4F4F4F',bd = 0.5,command = lambda:int810())
        btnf.place(x = 186,y = 147.5,width = 94,height = 27.5)       
        btnac = tkinter.Button(root,text = 'AC',font = ('微软雅黑',20),fg = 'orange',bd = 0.5,command = lambda:pressCompute('AC'))
        btnac.place(x = 0,y = 340,width = 70,height = 55)
    if model == '亲戚关系':
        box1 = easygui.buttonbox("称呼方式：",choices = ['我称呼对方','对方称呼我'])
        if box1 == '我称呼对方':
            r=0
        else:r=1
        box2 = easygui.buttonbox("我的性别：",choices = ['男','女'])
        if box2 == '男':
            s=1
        else:s=0
        box3 = easygui.enterbox('请输入关系')
        text = box3
        g = relation.get_relation({'text':text, 'sex':s, 'reverse':r})
        easygui.msgbox('、'.join(g))
#操作函数
lists = []#设置一个变量，保存运算数字和符号的列表
isPressSign = False#添加一个判断是否按下运算符号的标志,假设默认没有按下按钮
isPressNum = False
Models=[]
#数字函数
def pressNum(num):
    global lists
    global isPressSign
    if isPressSign == False:
        pass
    else:#重新将运算符号状态设置为否
        result.set(0)
        isPressSign = False

#判断界面的数字是否为0
    oldnum = result.get()#第一步
    if oldnum =='0':#如过界面上数字为0 则获取按下的数字
        result.set(num)
    else:#如果界面上的数字不是0  则链接上新按下的数字
            newnum = oldnum + num
            result.set(newnum)#将按下的数字写到面板中


#运算函数
def pressCompute(sign):
    global lists
    global isPressSign
    num = result.get()#获取界面数字
    lists.append(num)#保存界面获取的数字到列表中
    result.set('')
    lists.append(sign)#讲按下的运算符号保存到列表中
    isPressSign = True

    if sign =='AC':#如果按下的是'AC'按键，则清空列表内容，将屏幕上的数字键设置为默认数字0
        lists.clear()
        result.set(0)
    if sign =='b':#如果按下的是退格‘’，则选取当前数字第一位到倒数第二位
        a = num[0:-1]
        lists.clear()
        result.set(a)
##################################################################################################################################杜卓凡
def apl2():#功能2进行实现
    root2 = tkinter.Tk()
    #fv，pv,t,pmt,r的标签显示
    tkinter.Label(root2, text="FV：").grid(row=0)
    tkinter.Label(root2, text="PV：").grid(row=1)
    tkinter.Label(root2, text="T：").grid(row=2)
    tkinter.Label(root2, text="PMT：").grid(row=3)
    tkinter.Label(root2, text="R：").grid(row=4)
    
    FV = tkinter.Entry(root2)
    PV = tkinter.Entry(root2)
    PMT = tkinter.Entry(root2)
    T = tkinter.Entry(root2)
    R = tkinter.Entry(root2)
    
    FV.grid(row=0, column=1, padx=10, pady=5)
    PV.grid(row=1, column=1, padx=10, pady=5)
    T.grid(row=2, column=1, padx=10, pady=5)
    PMT.grid(row=3, column=1, padx=10, pady=5)
    R.grid(row=4, column=1, padx=10, pady=5)
    Result2 =tkinter.Text(root2,height = 5, width =30)
    Result2.grid(row=5, column=0, columnspan=3)
    
    def compute1():#计算函数
        #产生一个获取输入内容的变量
        fv1= FV.get()
        pv1 = PV.get()
        pmt1 = PMT.get()
        r1 = R.get()
        t1 = T.get()
        count = 0#记录参数长度为0的计数器
        
        def annuity(pram1,fv1,pv1,pmt1,r1,t1):
            if pram1 == fv1 :
                pv = float(pv1)#为了计算，类型转换为float型
                pmt = float(pmt1)
                r = float(r1)/100
                t = int(t1)
                sum = pv 
                for i in range (0,t):
                    sum = sum*(1+r) +pmt
                Result2.insert("insert","FV计算结果为:{}".format(sum))
                
            if pram1 == pv1 :
                fv = float(fv1)
                pmt = float(pmt1)
                r = float(r1)/100
                t = int(t1)                
                sum = fv
                for i in range(0,t):
                        sum = (sum - pmt)/(1+r)
                Result2.insert("insert","PV计算结果为:{}".format(sum))
                
            if pram1 == pmt1 :
                fv = float(fv1)
                pv = float(pv1)
                r = float(r1)/100
                t = int(t1)     
                sum = fv - pv*(1+r)^t
                sum2 = 0
                for i in range(0,t):
                    sum2 = sum2*(1+r) + 1
                    sum = sum/sum2
                Result2.insert("insert","pmt计算结果为:{}".format(sum))
                
            if pram1 == t1 :
                fv = float(fv1)
                pv = float(pv1)
                pmt = float(pmt1)
                r = float(r1)/100
                sum = pv
                for n in range (1,10000):
                    sum = sum*(1+r) + pmt
                    if sum > fv:
                       Result2.insert("insert","无法达成,t接近:{}".format(n))
                       return 0
                    elif sum == fv:
                        Result2.insert("insert","t计算结果为:{}".format(n))
                        return 0
                    else :
                        n = n+1
                
                Result2.insert("insert","r计算结果为:")
        
        for item in {fv1,pv1,pmt1,r1,t1}:
            if len(item) == 0  :#判断输入参数的长度是否为0，如为0，则计算此参数
                count += 1
                pram = item
            if count == 2 :#参数个数不足以计算，发出提醒
                Result2.insert("insert","请输入至少四个参数!")
                return 0
            if item.isdigit() == False and item != pram:#参数中存在不是数字的字符，予以提醒
                Result2.insert("insert","您输入的参数中有非法字符，请检查!")
                return 0
        annuity(pram,fv1,pv1,pmt1,r1,t1)
            
    def reset() :
        for item2 in {FV,PV,PMT,R,T} :
            item2.delete(0,"end")
        Result2.delete(1.0,'end')
                                                              
    tkinter.Button(root2, text="计算", width=10, command=compute1).grid(row=6, column=0,  padx=10, pady=5)
    tkinter.Button(root2, text="退出", width=10, command=root2.destroy).grid(row=6, column=1, padx=10, pady=5)
    tkinter.Button(root2, text="重置", width=10, command=reset).grid(row=6, column=2, padx=10, pady=5)
    
def apl3():
    root3 = tkinter.Tk()
    root3.title('简单数据特征分析')
    
    tkinter.Label(root3, text=" a: ").grid(row=2)
    tkinter.Label(root3, text=" b: ").grid(row=3)
    tkinter.Label(root3, text="请输入以,(英文逗号)隔开的数字").grid(row=0,column =1)
    tkinter.Label(root3, text="此功能可以计算两数组的均值方差，以及两组的相关系数和协方差").grid(row=1,column =0,columnspan =3)
    
    a = tkinter.Entry(root3)
    a.grid(row=2 ,column =1 ,padx=10, pady=10)
    b = tkinter.Entry(root3) 
    b.grid(row=3 ,column =1, pady=10)
    
    def Anls():
        a_temp = a.get()
        a1 = a_temp.split(",")#产生仅包含输入数字的字符串，以便计算
        a_len = len(a1)
        suma = 0
        a_var_sum = 0
        for i in a1 :
            a2 =Decimal(i)#类型转换以便计算
            suma += a2
        a_ave = suma/a_len
        for o in a1 :
            a3 =Decimal(o)
            a_var_sum += pow((a3 - a_ave),2)
        a_var = round(a_var_sum/a_len,8)
        
        c.insert(1.0,"a均值为"+str(a_ave)+"       a的方差为:{}".format(a_var))
        c.insert(tkinter.INSERT, '\n')
        
        b_temp = b.get()
        b1 = b_temp.split(",")#产生今年仅包含输入数字的字符串，以变计算
        b_len = len(b1)
        sumb = 0
        b_var_sum = 0
        for p in b1 :
            b2 =Decimal(p)#类型转换以便计算
            sumb += b2
        b_ave = sumb/b_len
        for q in b1 :
            b3 =Decimal(q)
            b_var_sum += pow((b3 - b_ave),2)
        b_var = round(b_var_sum/b_len,8)
        
        c.insert(2.0,"b均值为"+str(b_ave)+"     b方差为:{}".format(b_var))
        c.insert(tkinter.INSERT, '\n')        
        
        b_dev =math.sqrt(b_var)
        a_dev =math.sqrt(a_var)
        sumab = 0
        for s in range (0,b_len) :
            a4 = float(a1[s])
            b4 = float(b1[s])
            print ()
            sumab += a4 * b4
        ab_ave = sumab/b_len
        covv1= ab_ave - float(a_ave * b_ave)
        covv = round(covv1,6)
        cor = covv /float(b_dev * a_dev)
        c.insert(3.0,"相关系数为："+str(cor)+"  协方差为："+str(covv))

    def reset3():
        a.delete(0,"end")
        b.delete(0,"end")
        c.delete(1.0,"end")
        
        
    tkinter.Button(root3, text="计算", width=10, command=Anls).grid(row=4, column=0, padx=10, pady=5)
    tkinter.Button(root3, text="返回", width=10, command=root3.destroy).grid(row=4, column=1, padx=10, pady=5)
    tkinter.Button(root3, text="重置", width=10, command=reset3).grid(row=4, column=2,padx=10, pady=5)
    c = tkinter.Text(root3, height = 10, width =50)
    c.grid(row=5 ,column=0 ,columnspan=3,padx=10, pady=5)

def apl4():
    root4 = tkinter.Tk()
    root4.title('投资方案比较')
    
    tkinter.Label(root4, text="方案1:").grid(row=2)
    tkinter.Label(root4, text="方案2:").grid(row=3)
    tkinter.Label(root4, text="请输入以,(英文逗号)隔开的现金流,请注意正负号,此功能可以计算irr").grid(row=0,column =0,columnspan =3)
    tkinter.Label(root4, text="如只计算一个方案，请在另一方案置1").grid(row=1,column =0,columnspan =3)
    
    
    a = tkinter.Entry(root4)
    a.grid(row=2 ,column =1 ,padx=10, pady=10)
    b = tkinter.Entry(root4) 
    b.grid(row=3,column =1, pady=10)
    
    def Anls():
        
        a_temp = a.get()
        a1 = a_temp.split(",")
        lista = []#产生一个列表将a1元素添加进去，以便于计算
        for i in a1 :
            lista.append(float(i))
        print (lista)
    
        b_temp = b.get()
        b1 = b_temp.split(",")
        listb = []#产生一个列表将a1元素添加进去，以便于计算
        for n in b1 :
            listb.append(float(n))
        
        irra = round(np.irr(lista),6)
        irrb = round(np.irr(listb),6)
        
        c.insert(1.0,"内部收益率IRR = {}%".format(irra*100))
        c.insert(tkinter.INSERT, '\n')
        c.insert(2.0,"内部收益率IRR = {}%".format(irrb*100))
        c.insert(tkinter.INSERT, '\n')
       
        if irra > irrb:
            c.insert(3.0,"选择方案1，因为它的irr更大")
        elif irra < irrb:
            c.insert(3.0,"选择方案2，因为它的irr更大")
        else:
            c.insert(3.0,"选择方案1,2皆可")
            

    def reset4():
        a.delete(0,"end")
        b.delete(0,"end")
        c.delete(1.0,"end")
        
        
    tkinter.Button(root4, text="计算", width=10, command=Anls).grid(row=4, column=0, padx=10, pady=5)
    tkinter.Button(root4, text="返回", width=10, command=root4.destroy).grid(row=4, column=1, padx=10, pady=5)
    tkinter.Button(root4, text="重置", width=10, command=reset4).grid(row=4, column=2,padx=10, pady=5)
    c = tkinter.Text(root4, height = 10, width =50)
    c.grid(row=5 ,column=0 ,columnspan=3,padx=10, pady=5)
################################################################################################################################徐凯成
#三角函数及ln
def sin():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    computrStr = float(computrStr)
    computrStr = math.radians(computrStr)
    endNum = math.sin(computrStr)
    endNum = '%.2f'%endNum
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def cos():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    computrStr = float(computrStr)
    computrStr = math.radians(computrStr)
    endNum = math.cos(computrStr)
    endNum = '%.2f'%endNum
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def tan():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    computrStr = float(computrStr)
    computrStr = math.radians(computrStr)
    endNum = math.tan(computrStr)
    endNum = '%.2f'%endNum
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def ln():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    computrStr = float(computrStr)
    endNum = math.log(computrStr,math.e)
    endNum = '%.2f'%endNum
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
#进制转换函数
def bin102():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = bin(int(computrStr,10))
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def int210():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = int(computrStr,2)
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def oct28():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = oct(int(computrStr,2))
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def bin82():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = bin(int(computrStr,8))
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def oct108():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = oct(computrStr)
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
def int810():
    global lists
    
    curnum=result.get()
    lists.append(curnum)
    computrStr = ''.join(lists)
    endNum = int(computrStr,8)
    result.set(endNum)
    result2.set(computrStr)
    lists.clear()
#获取运算结果函数
def pressEqual():
    global lists
    global isPressSign


    curnum = result.get()#设置当前数字变量，并获取添加到列表
    lists.append(curnum)

    computrStr = ''.join(lists)#讲列表内容用join命令将字符串链接起来
    endNum = eval(computrStr)#用eval命令运算字符串中的内容
    endNum = '%.2f'%endNum
    result.set(endNum) #讲运算结果显示到屏幕1
    result2.set(computrStr)#将运算过程显示到屏幕2
    lists.clear()#清空列表内容
################################################################################################################################杜卓凡
#功能菜单
men =tkinter.Menu(root)#创建菜单
men.add_command(label ="金融函数",command=apl2)
men.add_command(label ="数据分析",command=apl3)
men.add_command(label ="投资分析",command=apl4)
men.add_command(label ="单位换算",command = lambda :pressModel('单位换算'))
men.add_command(label ="亲戚关系",command = lambda :pressModel('亲戚关系'))
men.add_command(label ="进制换算",command = lambda :pressModel('进制换算'))
men.add_command(label ="返回",command = lambda :pressModel('返回'))
root.config(menu = men)
root.mainloop()
