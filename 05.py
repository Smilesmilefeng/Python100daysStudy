'''
# 寻找水仙花数
for num in range(100,1000):
    low = num%10
    mid = num//10%10
    high = num//100
    if num == low**3 + mid**3 + high**3:
        print(num)
'''

#正整数的反转
num = 12345
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10
print(reversed_num)

#Fibonacci sequence
sum1 = 1
sum2 = 1
print('Fibonacci sequence:\n1\n1')
for i in range(1,21):
    sum = sum1 + sum2
    sum1 = sum2
    sum2 = sum
    print(sum)