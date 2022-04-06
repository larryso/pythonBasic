# This is a sample Python script.
from math import exp, log, sqrt
import time
import calendar
from datetime import date, datetime, timedelta
from basic import fibonacci_demo, file_utils
import sys

from basic.file_utils.file_utils import dir_travel, append_write2file
from basic.thread_test.threadTest import MyThread
from basic.csv_process.csv_read_with_simple_parsing_and_write import csv_simple_read_write
from basic.csv_process.pandas_parsing_and_write import csv_pandas_read_write

import glob
from basic.excel_process.base_excel_read_write import excel_read_write
from basic.excel_process.pandas_excel_read_write import pandas_excel_read_write


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

    ## encode decode method
    string5 = "拉里"
    string5_utf_8 = string5.encode("utf-8")
    print(f"UTF-8 encoding is: {string5_utf_8}")
    print("decoding is: {0}".format(string5_utf_8.decode("UTF-8")))

    #join method
    str_sequence =("L", "A", "R", "R", "Y")
    str_joiner = "-"
    print(f"joined string is: {str_joiner.join(str_sequence)}")

    ## stip method
    random_string = 'this is good    '
    print(f"rstrip after: {random_string.rstrip()}") # rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。
    str = "*****this is string example....wow!!!*****"
    print(str.rstrip('*'))

    ## replace method
    lix_url = "https://infox.swissre.com"
    print(f"new lix url is: {lix_url.replace('infox.swissre.com', 'lix.swissre.cn')}")

def dateTest():
    ## Print current time stamp since 1970
    current_time_stamp = time.time()
    print(current_time_stamp)

    ## print local time
    local_time = time.localtime(time.time())
    print(f"Local time {local_time}")

    ## format time
    print(time.asctime(time.localtime(time.time())))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    cal = calendar.month(2016, 1)
    print("以下输出2016年1月份的日历:")
    print(cal)

    ### demo datetime module
    today = date.today()
    print(f"Output #1 Today is: {today}")
    print(f"Output #2 Today year is: {today.year}")
    print(f"Output #1 Today month is: {today.month}")

    one_day = timedelta(days=-1)
    yestoday = today + one_day
    print(f"Yestoday is {yestoday}")
    date_diff = today - yestoday
    print(date_diff)
    print(str(date_diff).split()[0])

def listTest():
    list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    print(f"The first element in the list is: {list[0]}")
    print(f"The last element in the list i: s{list[-1]}")
    list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
    # 从第二位开始（包含）截取到倒数第二位（不包含）
    print("list[1:-2]: ", list[1:-2])
    print(f"list from the first to the third: {list[0:3]}")
    list[4] = "Baidu"
    list.append("Microsoft")
    print(list)
    del list[3]
    print(list)
    # list copy
    list2 = list[:]
    print(list2)
    list3 = [1,2,3]
    print(list2 + list3)
    # 嵌套列表
    a = ['a', 'b', 'c']
    n = [1,2,3]
    x = [a, n]
    print(x)
    print(x[0][1]) #b
    list5 = ['a', 'b', 'c']
    list5.insert(2,'e')
    print(list5)
    list5.pop(2)
    print(list5)
    list5.reverse()
    print(list5)

def tupleTest():
    tuple1 = ("Google", "Yourtub")
    print(tuple1)

    empty_tuple = () # defined an empty tuple

    single_va_tuple = ('Larry') #元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
    print(type(single_va_tuple))
    single_va_tuple = ('Larry',)
    print(type(single_va_tuple))

    ## convert a pule to a list / or convert list to tuple
    list = ["x", 'y', 'z']
    to_tuple = tuple(list)
    print(to_tuple)

def setTest():
    list1 = ["Google", "Microsoft", "YourTube"]
    list2 = ["Google", "Microsoft", "YourTube", "Amazon"]
    print(list1 + list2)
    set1 = {"Google", "Microsoft", "YourTube"}
    set1.add("Google")
    print(set1)
    set2 = {"Google", "Microsoft", "YourTube", "Amazon"}
    print(set2 - set1)
    print("Google" in set1)

def dictionaryTest():
    empty_dic = {}
    a_dict = {"one": 1, "two":2, "three":3}
    print(a_dict)
    another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle',9]}
    print(another_dict)
    print(another_dict.values())
    print(another_dict.items())
    if "x" in another_dict:
        print("X is one key in another_dict")

    for key in another_dict:
        print(another_dict.get(key))

def flowControl():
    ## while loop and for loop
    numbers = [23,45,66,78,90,112]
    even = []
    odd = []
    while(len(numbers) >0):
        number = numbers.pop()
        print(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print(even)
    print(odd)
    numbers = [23, 45, 66, 78, 90, 112]
    even.clear()
    odd.clear()
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print(even)
    print(odd)
    i = 0
    while True:
        i += 1
        print(i)
        if i == 200000:
            continue
        if i==300000:
            break

def exceptionTest():

    try:
        fh = open("D://test//test.txt", "w")
        fh.write("This is a test file")
    except IOError as e:
        raise e
        # print("!! Error, file not found")

    else:
        print("File write with success..")
    finally:
        try:
            fh.close()
        except:
            pass

def dummyMethod():
    pass

def variableTest(num):
    print("-" * 50)
    print("%d 在函数内的内存地址是 %x" % (num, id(num)))
    result = 10
    print("%d 在函数内的内存地址是 %x" % (result, id(result)))
    print("-" * 50)
    return result

def yieldTest():
    print("Starting...")
    while True:
        result = yield 4
        print(f"Result: {result}")

def iterTest():
    list = [1,2,3,4,5]
    it = iter(list)
    for i in it:
        print(i)
    it2 = iter(list)
    while True:
        try:
            print(next(it2))
        except StopIteration:
            sys.exit()

def glob_test(dir_path):
    f = glob.glob(dir_path)
    print(f)

    for file in f:
        print(file)

def iglob_test(dir_path):
    f = glob.iglob(dir_path)
    print(f)

    for file in f:
        print(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #numberTest()
    #stringTest()
    # dateTest()
    # listTest()
    # tupleTest()
    # setTest()
    # dictionaryTest()
    # flowControl()
    # try:
    #     exceptionTest()
    # except IOError as e:
    #     print("!! Exception !!")

    #fibonacci_demo.fibonacciDemo1(3)
    # for i in
    # range(20):
    #     print(fibonacci_demo.fibonacciDemo2(i))

    # for i in range(10):
    #     print(fibonacci_demo.fibonacciDemo4(i))

    # 1 Variable
    # test a, b = b, a+b
    #  对于python而言，python的一切变量都是对象，变量的存储，采用了引用语义的方式，存储的只是一个变量的值所在的内存地址，而不是这个变量的只本身
    # a, b = 0, 1
    # print(id(a))
    # print(id(b))
    # for i in range(3):
    #     a, b = b, a+b
    #     print(a)
    #     print(b)
    # a = 20
    # print("%d 调用函数前内存值为 %x" % (a, id(a)))
    # r = variableTest(a)
    # print("调用函数后 实参内存地址是 %x" % id(a))
    # print("调用函数后 返回值内存地址是 %x" % id(r))
    # a = 1
    # print("调用函数前内存值为 %x" % (id(a)))
    # a = "hello"
    # print("调用函数前内存值为 %x" % (id(a)))
    # a = [1, 2, 3]
    # print("调用函数前内存值为 %x" % (id(a)))
    # a = [3, 2, 1]
    # print("调用函数前内存值为 %x" % (id(a)))
    #
    # demo_list = [1, 2, 3]
    #
    # print("定义列表后的内存地址 %d" % id(demo_list))
    #
    # demo_list.append(999)
    # demo_list.pop(0)
    # demo_list.remove(2)
    # demo_list[0] = 10
    #
    # print("修改数据后的内存地址 %d" % id(demo_list))
    #
    # demo_dict = {"name": "小明"}
    #
    # print("定义字典后的内存地址 %d" % id(demo_dict))
    #
    # demo_dict["age"] = 18
    # demo_dict.pop("name")
    # demo_dict["name"] = "老王"
    #
    # print("修改数据后的内存地址 %d" % id(demo_dict))

    ######## yield test #########
    # result = yieldTest() # yieldTest 方法不会被执行，只是返回一个生成器 对象
    # print(f"yield return: {result}")
    # print(next(result))
    # print("*" * 20)
    # print(next(result))
    # print(result.send(7))

    ## Test python iter
    ##iterTest()

    ### Thread testing
    # threads = []
    # myThread1 = MyThread(1, "MyThread-1", 1)
    # myThread2 = MyThread(2, "MyThread-2", 2)
    # myThread3 = MyThread(3, "MyThread-3", 3)
    #
    # threads.append(myThread1)
    # threads.append(myThread2)
    # threads.append(myThread3)
    #
    # myThread1.start()
    # myThread2.start()
    # myThread3.start()
    #
    # # for t in threads:
    # #     t.join()
    #
    # print("############ exit main thread ###############")
    #print(dir_travel("F:\\temp\\python_test"))
    #append_write2file("F:\\temp\\python_test\\csv", "test_f_w.txt", "Hello 123456")

    # glob_test(r"c:\*")
    # iglob_test(r"c:\*")

    ##file_utils.file_utils.read_multiple_txt("C:\\tmp\\logs")
    #csv_simple_read_write("F:\\temp\\python_test\\csv\\csv_sample.csv", "F:\\temp\\python_test\\csv\\csv_sample2.csv")
    ##csv_pandas_read_write("F:\\temp\\python_test\\csv\\csv_sample.csv",  "F:\\temp\\python_test\\csv\\csv_sample3.csv")
    #excel_read_write("F:\\temp\\python_test\\excel\\test.xlsx", "F:\\temp\\python_test\\excel\\test_out.xlsx")
    #pandas_excel_read_write("F:\\temp\\python_test\\excel\\test.xlsx", "F:\\temp\\python_test\\excel\\test_out_pandas.xlsx")











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
