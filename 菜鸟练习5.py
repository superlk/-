#!/usr/bin/env python
#_*_coding:utf-8_*_
# ��Ŀ��������������x,y,z���������������С���������
# ���������������취����С�����ŵ�x�ϣ��Ƚ�x��y���бȽϣ����x>y��x��y��ֵ���н�����Ȼ������x��z���бȽϣ����x>z��x��z��ֵ���н�����������ʹx��С��
# ˼·�� �������x��y��zת��Ϊint��Ȼ������б�Ȼ��ð�����򣬻���max����Ȼ���������ӡ

def sort_num():
    my_list=[]
    x=int(raw_input('x����������'))
    y=int(raw_input('y,��������'))
    z=int(raw_input('z,��������'))
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

