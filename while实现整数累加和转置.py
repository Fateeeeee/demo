import random

'''
#实现100以内数累加
i=0
sum=0
while i<100:
    sum=sum+i
    i=i+1
print(sum)
'''
#100~100000内整数转置
n=input("请输入100-100000的整数")
n=int(n)
b=0
while n>0:
    b=b*10+n%10
    n=n//10
print(b)


