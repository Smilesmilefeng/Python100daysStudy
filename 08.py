class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, courseName):
        print('%s正在学习%s.' % (self.name, courseName))

    def watchMovie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('python程序设计')
    # 给对象发watchMovie消息
    stu1.watchMovie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watchMovie()


# if __name__ == '__main__':
#     main()


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


# def main():
#     test = Test('hello')
# AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()
# AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)

# if __name__ == '__main__':
#     main()


def main():
    test = Test('hello1')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()

# 练习: 定义一个类描述数字时钟
from time import sleep


class Clock(object):
    # 数字时钟
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 55)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()