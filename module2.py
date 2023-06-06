# print('call module1')
def printModuleName():
    print('call printModuleName:module2')

print(__name__)
if __name__ == '__main__':
    printModuleName()