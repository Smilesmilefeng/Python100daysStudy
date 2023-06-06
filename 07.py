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