import os

print(os.path.abspath('.'))
print(__file__)

import sys

def add(x, y):
    return x + y
x = 1
y = 2
z = add(x, y)
print(z)
print(sys.argv) # sys.argv 是用来获取从命令行传递给脚本的参数的，上面的x，y不被包含在其中

print(sys.executable)  # sys.executable 是用来获取当前 Python 解释器的路径的
print(sys.path)        # sys.path 是用来获取当前 Python 解释器的模块