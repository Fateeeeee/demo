from random import randint  #import库中某个函数
import random    #import整个库

a=randint(10,100)
b=randint(10,100)

print(a,b)

'''
#交换a,b的值（改变值）
if a<b:
    a,b=b,a
print(a,b)
'''

#交换a，b的值，不改变值
if a>b:
    print(a,b)
else:
    print(b,a)

#a=0
a=a<b
if a:#输出a是True为bool类型或者False
    print(a)
else:
    print(a)
