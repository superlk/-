#!/usr/bin/env python
#_*_coding:utf-8_*_
#date：2017-7-28
#mail：651002081@qq.com
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
#低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
#40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
#超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
I=int(raw_input('请输入当月利润(单位/万):'))
if I <=10:
    j=I*0.1
elif I>10 and I<=20:
    j=10*0.1+(I-10)*0.075
elif I>20 and I<=40:
    j=10*0.1+10*0.075+(I-20)*0.05
elif I>40 and I<=60:
    j=10*0.1+10*0.075+20*0.05+(I-40)*0.03
elif I>60 and I<=100:
    j=10*0.1+10*0.075+20*0.05+20*0.03+(I-60)*0.015
else:
    j=10*0.1+10*0.075+20*0.05+20*0.03+40*0.015+(I-100)*0.01
print j
