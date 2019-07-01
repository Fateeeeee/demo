'''
1、join()函数
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
'''
test = ["I", "Like", "Python"]
print(test)
print("".join(test)) # 表示分隔符为空合并字符串数组为一个字符串