#!/usr/bin/env python
#_*_coding:utf-8_*_
# ��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
# �����������3��5��Ϊ����Ӧ���Ȱ�ǰ�����µļ�������Ȼ���ټ���5�켴����ĵڼ��죬��������������������·ݴ���2ʱ�迼�Ƕ��һ��
# ����������1�����Ա�4���������ǲ��ܱ�100������2�����Ա�400������ÿ4��һ����100������400����
your_date=raw_input('������������(��ʽΪ2017-3-18)��') 
your_date_lsit=your_date.split('-')
month=(0,31,59,90,120,151,181,212,243,304,334)
# �ж��¶�Ӧ����
if 0<int(your_date_lsit[1])<12:  
    sum=month[int(your_date_lsit[1])-1]
else:
    print 'your input error'
 
# ��������������    
sum+=int(your_date_lsit[2])

# �ж����꣬���´���2 ��sum+1
if (int(your_date_lsit[0])%4==0 and int(your_date_lsit[0])%100 !=0) or  (int(your_date_lsit[0])%400==0):
    if int(your_date_lsit[1])>2:
           sum+=1
# ��ӡ������
print '��һ��ĵ�%s��'%sum

