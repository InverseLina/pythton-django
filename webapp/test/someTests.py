# encoding=utf-8
import re, functools, timeit, datetime, time
__author__ = 'Hinsteny'


# 1.编写代码，打印1-1亿之内的偶数
def question_one():
    maxV = 100000001
    # 列表生成式
    data = [ x for x in range(1, 10) if x % 2 == 0]
    for x in data:
        print(x)
    # 迭代器
    g = (x for x in range(1, maxV) if x % 2 == 0)
    for n in g:
        print(n)

# 2.写一个函数，用正则表达式清除字符串中[]合其中的内容
def question_two():
    dataStr = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"
    re_str = re.compile(r'\[.*?\]')
    str = re_str.sub('', dataStr)
    print(str)

# 3.打印函数被调用时的耗时详情
def question_three():
    def log():
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("<function name: %s>" % func.__name__)
                print("<function call begin>")
                date_start = timeit.default_timer()
                result = func(*args, **kw)
                date_end = timeit.default_timer()
                print("<function call end>")
                time_variance = date_end - date_start
                print("[timecosts: %s]" % time_variance)
                return result
            return wrapper
        return decorator

    @log()
    def hello(name):
        print("hello, %s" % name)

    hello("python")

# 4. 将驼峰命名法字符串转换成下划线命名字符串
def question_four():
    def addpter(name):
        re_str = re.compile(r'[A-Z]{1}')
        strs = re_str.split(name)
        for x in strs:
            print(x)
        return name
    def find(name):
        re_str = re.compile(r'[A-Z]{1}')
        index = name.find(re_str)
        while index > 0:
            print(index)
            index = name.find(re_str)
    data = ["GetItem", "getItem", "doIT", "doWork"]
    for x in data:
        #addpter(x)
        find(x)


if __name__ == "__main__":
    #question_one()
    #question_two()
    #question_three()
    question_four()