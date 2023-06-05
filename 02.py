"""
使用type()检查变量的类型

Version: 0.1
Author: 骆昊
"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>


"""
使用input()函数获取键盘输入（字符串）
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))


# 将华氏度转换为摄氏度

# f = float(input('请输入华氏温度：'))
# c = (f - 32) /1.8
# print('%.3f华氏度 = %.2f摄氏度' % (f,c))


#计算圆的周长和面积
radius = float(input('请输入圆的半径：'))
pi = 3.14159
perimeter = 2 * pi * radius
area = pi * radius * radius
print('圆的周长是%.2f' % perimeter)
print('圆的面积是%.2f' % area) 