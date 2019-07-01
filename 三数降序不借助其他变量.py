import random


a=random.randint(10,100)
b=random.randint(10,100)
c=random.randint(10,100)

'''
1.通过创建list列表来调用sorted函数来排序
list=[a] #创建一个列表
list.append(b) #添加列表
list.append(c)
'''
'''
list=[a,b,c]
test=sorted(list,reverse=True)  #reverse为True表示逆序排列
'''
'''
2.通过自带的交换值a,b=b,a实现改变
'''
'''
if a<b:
    a,b=b,a
if a<c:
    a,c=c,a
if b<c:
    b,c=c,b
'''
'''
3.不改变值的if elif else来排序,列出所有情况，或者先通过一个大的if else分出一种情况(确定一种),再对其下面的进行划分即2*3种情况
'''
'''
if a<b<c:
    print(c,b,a)
elif a<c<b:
    print(b,a,c)
elif b<a<c:
    print(c,a,b)
elif c<a<b:
    print(b,a,c)
elif b<c<a:
    print(a,c,b)
elif c<b<a:
    print(a,b,c)
'''
if a>b:
    if c>a:#此时a较大，故先定出c>a情况
        print(c,a,b)
    elif b>c:#此时排除了c<a情况即定出了a>b，且c<a
        print(a,b,c)
    else:#排除了上面两种情况，那肯定就是b<c<a情况了
        print(a,c,b)
else:
    if c>b:
        print(c,b,a)
    elif c>a:
        print(b,c,a)
    else:
        print(b,a,c)
