# encoding=utf-8

__author__ = 'Hinsteny'




import sys
import time
import timeit
default_timer = None

if sys.platform == "win32":
# On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
# On most other platforms the best timer is time.time()
    default_timer = time.time
print(default_timer)
timeIn= time.clock()
for i in range(100):
    n=i
timeUse = time.clock()-timeIn
print(timeUse)

timeIn = time.time()
for i in range(100):
    n=i
timeUse = time.time()-timeIn
print(timeUse)

timeIn = timeit.default_timer()
for i in range(100):
    n=i
timeUse = timeit.default_timer()-timeIn
print("timeuser %s" % timeUse)



#该段代码在windows下结果如下
# >>>
# 4.07873067161e-005
# 0.0
# 3.5758734839e-005

#因为time.clock() 返回的是处理器时间，而因为 Unix 中 jiffy 的缘故，所以精度不会太高。
#因此，在Windows 系统中，建议使用 time.clock()，在Unix 系统中，建议使用 time.time()，
#而使用timeit代替 time，就可以实现跨平台的精度性，使用timeit.default_timer()函数来获取时间