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
'''
multiple lines comments 
'''
def stringTest():
    ## python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
    multiple_lines_str = ''' 
    this is a multiple lines string
    this is the second line
    this is the third line 
    TAB (\t) this is the forth line
    '''
    print(multiple_lines_str)

    string1 = "This is a "
    string2 = "short string"
    sentence = string1 + string2
    print("Output #10 %s" % sentence)

    string3 = "My delivrable is due in May"
    string3_list = string3.split(" ")
    string3_list_2 = string3.split(" ",2)
    print(string3_list)
    print(string3_list_2)
    string4 = "Your,deliverable,is,due,in,June"
    string4_list = string4.split(",")
    print("The second word is: %s" % string4_list[1])
    print(string4_list[-1])
    print(f"The last word in this string is {string4_list[-1]}") # f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。之前我们习惯用百分号 (%):

    string5 = "拉里"
    string5_utf_8 = string5.encode("utf-8")
    print(f"UTF-8 encoding is: {string5_utf_8}")
    print("decoding is: {0}".format(string5_utf_8.decode("UTF-8")))

    str_sequence =("L", "A", "R", "R", "Y")
    str_joiner = "-"
    print(f"joined string is: {str_joiner.join(str_sequence)}")

    random_string = 'this is good    '
    print(f"rstrip after: {random_string.rstrip()}") # rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
    str = "*****this is string example....wow!!!*****"
    print(str.rstrip('*'))

    lix_url = "https://infox.swissre.com"
    print(f"new lix url is: {lix_url.replace('infox.swissre.com', 'lix.swissre.cn')}")

def dateTest():




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # numberTest()
    stringTest()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
