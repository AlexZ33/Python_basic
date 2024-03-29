'''
Author: your name
Date: 2021-10-19 10:44:56
LastEditTime: 2021-10-19 11:07:31
LastEditors: Please set LastEditors
Description: https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
FilePath: /Python_basic/装饰器/property.py
'''


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。


def now():
    print("2021-0808")


f = now

f()

# 函数对象有一个__name__属性，可以拿到函数的名字：

print(now.__name__)
print(f.__name__)


# 我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    """
    观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
    """

    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("20210808")


#   调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

now()


# 把@log放到now()函数的定义处，相当于执行了语句　now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')

now()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)

