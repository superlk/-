#!/usr/bin/env python
#_*_coding:utf-8_*_
# ��Ŀ��쳲��������С�
# ���������쳲��������У�Fibonacci sequence�����ֳƻƽ�ָ����У�ָ��������һ�����У�0��1��1��2��3��5��8��13��21��34��������
# ����ѧ�ϣ��Ѳ������������Եݹ�ķ��������壺
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)
num0=0
num1=1
n=2
for i in range(10):
    num0=num1+num0
    num1=num1+num0
    n+=1
    print num0
    print num1 

        
    