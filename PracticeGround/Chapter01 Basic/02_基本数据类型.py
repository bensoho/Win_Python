
## Python中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# Python 3中有六个标准的数据类型： 
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionaries（字典）


# Numbers（数字）
# Python 3支持int、float、bool、complex（复数）。 
# 数值类型的赋值和计算都是很直观的，就像大多数语言一样。
# 内置的type()函数可以用来查询变量所指的对象类型。 
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# String（字符串）
# Python中的字符串str用单引号(' ')或双引号(" ")括起来，同时使用反斜杠(\)转义特殊字符。
s = 'Yes,he doesn\'t'
print(s,type(s),len(s))
# 如果你不想让反斜杠发生转义，可以在字符串前面添加一个r，表示原始字符串：
s1 = r'Yes,he doesn\'t'
print(s1,type(s1),len(s1))

print('str'+'ing','my'*5)

print(s[0],s[-1])

# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表是写在方括号之间、用逗号分隔开的元素列表。列表中元素的类型可以不相同：
a = ['wangming', 15, 10, 'dog']
print(a)

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。 
# 元组中的元素类型也可以不相同： 
a = (1991, 2014, 'physics', 'math')
print(a)

# Sets（集合）

# 集合（set）是一个无序不重复元素的集。
# 基本功能是进行成员关系测试和消除重复元素。
# 可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)



# Dictionaries（字典）

# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 字典是一种映射类型（mapping type），它是一个无序的键 : 值对集合。
# 关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字。
# 在同一个字典中，关键字还必须互不相同。
dic = {}  # 创建空字典
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel['Jack'])
for key,value in tel.items():
    print(key,value)

