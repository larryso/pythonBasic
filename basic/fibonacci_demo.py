'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：0,1、1、2、3、5、8、13、21、34、……在数学上，
斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
'''

def fibonacciDemo1(n):
    n1, n2 = 0, 1
    count = 0
    if n < 0:
        print("Please input a positive number!")
    elif n ==0:
        print(f"Fibonacci Sequence up to {n} is:")
        print(0)
    else:
        print(f"Fibonacci Sequence up to {n} is:")
        while count <= n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

def fibonacciDemo2(n):
    assert n >= 0, "n must positive"
    if n <= 1:
        return n
    else:
        return fibonacciDemo2(n-1) + fibonacciDemo2(n-2)

def fibonacciDemo3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b #先计算 b = a+b, 后赋值给 a （ a = b)
    return a

## 递推法
# take n = 4 for example, 0, 1, 1, 2, 3
# a = 0, b = 1, a+b =1, b + a+b = 2, a=b +b +a+b  =3
def fibonacciDemo4(n):
    assert n>=0, "n must be positive integer!"
    if n ==0:
        return n
    else:
        a, b = 0, 1
        counter = 0
        while counter < n:
            temp = a + b
            b = a
            a = temp
            counter += 1
        return a
def fibonacciDemo5(n):
    assert n>=0, "n must be positive integer!"
    a, b = 0, 1
    while n >=0:
        a, b = b, a+b
        n -= 1
    yield a


