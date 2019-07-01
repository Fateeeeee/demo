import random




#生成随机数组
list=[]
for i in range(10):
    list.append(random.randint(1,100))
print(list)

#对随机数组遍历并找最值
max=0
min=100
sum=0
for i in range(10):
    if list[i]>max:
        max=list[i]
    if list[i]<min:
        min=list[i]
    sum+=list[i]

print("max=",max,"min=",min,"总和",sum) #用逗号隔开字符串和数字，可以输出它们而不输出逗号

#对list排序
list=sorted(list)
print("排序好的数组",list)
#插入数仍有序
'''
#普通插入
num=50
index=0
for i in range(10):
    if num<list[i]:#找出下标
       index=i
       break
list.insert(index,num)#插入
'''
#折半插入
num=50 #插入的数字
left=0
right=len(list)-1
while(left<=right):
    middle=(left+right)//2  #//表示整数除法，结果返回整数，这样才能作为数组下标
    if list[middle]>num:
        right=middle-1
    else:
        left=middle+1
list.insert(left,num)


'''
num=50
i=8
#关键是怎么增长数组
while i>0:
    if list[i]>num:
        list[i+1]=list[i]  #插入排序（如果数组值大于插入值，则该数组值向后移动留出空给插入值）。从后往前用前一个覆盖后一个，然后前一个的值用插入值覆盖
        list[i]=num
    i=i-1
'''
print("插入50后的数组",list)