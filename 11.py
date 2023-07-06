#文件和异常
import time

# def main():
#     f = None
#     try:
#         f = open('致橡树.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定文件')
#     except LookupError:
#         print('指定了未知编码')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误')
#     finally:
#         if f:
#             f.close()

# def main():
#     print('一次性读取整个文件内容')
#     with open('致橡树.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#     print('通过for-in循环逐行读取')
#     with open('致橡树.txt', mode='r', encoding='utf-8') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#     print('读取文件按行读取到列表中')
#     with open('致橡树.txt', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
""" 写入素数"""
from math import sqrt


def is_prime(n):
    '''判断素数的函数'''
    assert n > 0
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写入文件错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


if __name__ == '__main__':
    main()
