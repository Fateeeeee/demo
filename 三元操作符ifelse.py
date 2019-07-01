
a=9
a=6 if a==9 else a==10  #就是if 条件 后面的正确条件写到了if前面
print(a)

# 列表推导
#代码解释
#如果m＞10则m^2，如果m＜10，则m^4，产生的每个数都放进数组中
x = [m**2 if m>10 else m**4 for m in range(50)]
print(x)