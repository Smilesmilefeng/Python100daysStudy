''''
# 用for循环实现1-100求和
sum = 0
for x in range(1, 101):
    sum += x
print(sum)

#猜数字
import random
answer = random.randint(1,100)
counter = 0
while True:
    counter+=1
    number = int(input('请输入0-100的数字：'))
    if number <answer:
        print('大一点')
    elif number>answer:
        print('小一点')
    else:
        print('BINGO!, 你一共猜了%d次' % counter)
        break
    if counter>7:
        print('你的智商余额明显不足，7次都没猜对')
        break

        '''
#输出乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%dx%d=%d' % (j, i, i * j), end='\t')
    print(end='\n')