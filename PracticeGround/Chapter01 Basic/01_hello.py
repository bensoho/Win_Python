import keyword
print('hello,world!')
# 查看python版本
# PS E:\PythonCode> python -V
# Python 3.7.0
# python保留字
# print(keyword.kwlist)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a,b=0,1
while b<100000:
    print(b,end=" ")
    a,b=b,a+b
