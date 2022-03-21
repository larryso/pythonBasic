# This is a sample Python script.
from math import exp, log, sqrt


def numberTest():
    ########### integer type
    x = 9
    print("Output #1: {0}".format(x))
    print("Output #1: %d" % x)

    print("My Name is {0}, I am {1} years old.".format("Larry", 32))
    print("My Name is {name}, I am {age} years old.".format(name="Larry", age=32))
    print("My Name is %s, I am %d years old" % ("Larry", 32))  # %字符：标记转换说明符的开始

    print("Output #2: %d" % 3 ** 4)
    print("Output #3: %d" % (int(8.4) / int(2.7)))

    # Float
    print("Output #4: %-5.3f" % (8.3 / 2.7))  # 转换字符- 表示左对齐，字符宽度为5，浮点数精度为3
    print("Output 5# %*.3f:" % (5, (8.3 / 2.7)))  # 如果是*（星号），则宽度会从值元组中读出
    print("Output 6#: %+-5.3f" % (8.3 / 2.7))  # + 字符前输出 +

    print("Output 7#: %f" % (exp(3)))  # 自然数e 的指数
    print("Output 8# %f" % (log(4)))  # 自然数e 的对数
    print("Output #9 %s" % sqrt(4))  # 平方根
    y = sqrt(4)
    print("Type of x is %s, Type of y is %s" % (type(x), type(y)))

def stringTest():



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberTest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
