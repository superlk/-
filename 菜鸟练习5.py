#!/usr/bin/env python
#_*_coding:utf-8_*_
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
# 思路： 把输入的x，y，z转换为int，然后放入列表，然后冒泡排序，或者max排序，然后再输出打印

def sort_num():
    my_list=[]
    x=int(raw_input('x，输入整数'))
    y=int(raw_input('y,输入整除'))
    z=int(raw_input('z,输入整数'))
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)
    num1=max(my_list)
    
    my_list.remove(my_list[my_list.index(num1)])
    num2=max(my_list)
    my_list.remove(my_list[my_list.index(num2)])
    num3=my_list[0]
    return '%s>%s>%s'%(num1,num2,num3)

def sort_num_v1():
    l = []
    for i in range(3):
        x = int(raw_input('integer:\n'))
        l.append(x)
    l.sort()
    return l


res=sort_num()
print res

