#顺点号程序 py3.8
#coding=utf-8
import os
import sys
import re
# import numpy as np
import tkinter as tk
from tkinter import filedialog
#通过re.split()方法，一次性拆分所有字符串
def go_split(s, symbol):
    # 拼接正则表达式
    symbol = "[" + symbol + "]+"
    # 一次性分割字符串
    result = re.split(symbol, s)
    # 去除空字符
    return [x for x in result if x]
#******************************************************
#主程序
#初始化参数
data=[]
symbol=','
root = tk.Tk()
#隐藏tk窗口
root.withdraw()
file_path = filedialog.askopenfilename()
n=eval(input("请输入一个整数\n"))
f=open(file_path,'r')
lines=f.readlines()
# print(lines)
data=lines
#去掉换行符号
for i in range(0,len(data)):
    data[i]= data[i].strip()
#去掉空字符
data=[i for i in data if i != ''] 
for i in range(0,len(data)):
    data[i]= go_split(data[i],symbol)
# data=[i for item in data for i in item]  二维数组变一维数组
m=len(data)
data[m-1][0]=n
for i in range(0,len(data)-1):
    data[i][0]=n
    i +=1
    n +=1
f.close()
f=open(file_path,'w')
for i in range(0,len(data)):
    for j in range(0,3):
        if  j==0:
            f.write('J')
            f.write(str(data[i][j]))
            f.write(',,')
        elif j== 1:
            f.write(str(data[i][j]))
            f.write(',')
        else:
            f.write(str(data[i][j])+'\n')
f.close()