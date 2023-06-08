s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

print('')
s1 = 'hello ' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)  #whether str'll' in str s1, print bool
print('good' in s1)

#从字符串取出指定位置的字符
str2 = 'abc123456'
print(str2[2])

#字符串切片
print('字符串切片')
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3::-1])

#格式化输出
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a,b,a*b))
print(f'{a} * {b} = {a * b}')

#list列表
list1 = [1, 3, 5, 7,100]
print(list1)
list2 = ['hello '] * 3
print(list2)
print(len(list1))
print(len(list2))
list1[2] = 300
print(list1)

for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)

for index, elem in enumerate(list1):
    print(index, elem)

print(list1)
list1.append(200)
print(list1)
list1.insert(1, 2)
print(list1)

if 5 in list1:
    list1.remove(5)

if 7 in list1:
    list1.remove(7) 
print(list1)    

list1.pop(0)
print(list1)
list1.pop(-1)
print(list1)
list1.clear()
print(list1)

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
print(list1)
list2 = sorted(list1)
print(list2)
list2 = sorted(list1,reverse=True)
print(list2)
list2 = sorted(list1, key=len)
print(list2)

f = [x for x in range(1,10)]
print(f)
f = [x + y for x in 'ABCD' for y in '1234567']
print(f)
import sys
print(sys.getsizeof(f))
f = (x + y for x in 'ABCD' for y in '1234567')
print(f)
print(sys.getsizeof(f))
for val in f:
    print(val, end = ', ')

print('')
#元组
t = ('刘峰', 28, True, 'liufeng')
print(t)
print(sys.getsizeof(t))
person = list(t)
print(person)

#字典
# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)


#练习1：在屏幕上显示跑马灯文字。
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.4)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()