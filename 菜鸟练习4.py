#!/usr/bin/env python
#_*_coding:utf-8_*_
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天
# 闰年条件，1，可以被4整除，但是不能被100整除，2，可以被400整除，每4年一闰，满100不闰，满400再闰
your_date=raw_input('请输入年月日(根式为2017-3-18)：') 
your_date_lsit=your_date.split('-')
month=(0,31,59,90,120,151,181,212,243,304,334)
# 判断月对应天数
if 0<int(your_date_lsit[1])<12:  
    sum=month[int(your_date_lsit[1])-1]
else:
    print 'your input error'
 
# 天数加上日期数    
sum+=int(your_date_lsit[2])

# 判断闰年，且月大于2 ，sum+1
if (int(your_date_lsit[0])%4==0 and int(your_date_lsit[0])%100 !=0) or  (int(your_date_lsit[0])%400==0):
    if int(your_date_lsit[1])>2:
           sum+=1
# 打印输出结果
print '这一年的第%s天'%sum

