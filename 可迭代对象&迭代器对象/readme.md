# 可迭代对象
![](./img/for循环.png)
首选确保for循环的in后面是一个可迭代对象，这样就能通过python内置函数`iter()`得到一个迭代器对象（iterator）

![](./img/iter.png)
![](./img/迭代器对象.png)
我们分别把列表list_test和字符串str_test分别得到一个迭代器
我们尝试传入数字看看
![](./img/int类型的对象不是可迭代对象.png)
这里抛出了异常，因为数字不是一个可迭代对象

那么问题来了，　为什么列表和字符串是可迭代对象?
因为这些对象满足了特殊的接口：
![](./img/列表下__开头.png)
迭代列表时候，我们看看了列表下__开头的方法,其中的__iter__()就是迭代协议的接口。我们在使用iter(list_test)时候实际内部调用了这个__iter__()函数
我们再看迭代字符串时候，**我们发现没有找到__iter__()** , 但是有__getIterm__()这个接口
![](./img/__getIterm.png)
我们再看看迭代的签名, 要么传入的参数（对象）本身有迭代器，要么是一个序列。　我们这里list__test本身就有迭代器，而str_test是有__getItem__这种序列的接口。
![](./img/序列.png)

# 迭代器对象
![](./img/迭代器对象2.png)
```python
for n in list_test: 
    print(n) 
```
所以我们就搞清楚了，for循环中先由iter(list_test)得到一个迭代器t,然后不停的调用next next next 直到捕获到一个`StopIteration` 异常，跳出循环。
这就是for循环的工作流程

# 案例实现
> 我们从天气应用抓取各个城市温度：
> 北京: 10~18
> 南京: 13~23
> 上海: 14~22
....
>如果一次性抓取所有天气再显示，显示一个城市气温时，会有很多延迟。并且浪费存储空间。　我们希望以“用时访问”的策略，能把所有城市气温封装到一个对象里面，需要时候再显示。
> 提示，　可用for语句进行迭代。　代码怎么实现?

解决思路
- 1. 实现一个迭代器对象Weatherlterator, next方法每次返回一个城市气温.（迭代完毕时候要抛出停止迭代异常）
- 2. 实现一个可迭代对象Weatherlterable, __iter__方法返回一个迭代器对象。
    
```python
def getWeather(city):
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['forecast'][0]
    # print(data)
    return '%s: %s, %s'%(city, data['low'], data['high'])

print(getWeather(u'南京'))
print(getWeather(u'上海'))
```
    
![](./img/结果.png)

以上是获取城市气温数据方法，下面我们实现迭代器对象和可迭代对象,在python标准库中对他们的接口已经有定义。

![](./img/python标准库.png)

在collections包下有
- Iterable(可迭代对象抽象接口就是`__iter__`)
- Iterator(迭代器抽象接口就是`__next__`)

我们可以直接继承这两个抽象类

```python
import requests
from collections import Iterable, Iterator


# 天气迭代器,
class WeatherIterator(Iterator):
    # 应该有个参数描述此迭代器能够返回哪些城市信息, 传入一个城市名字符串列表cities
    def __init__(self, cities):
        self.cities = cities
        # 记录迭代的位置，初始化为０
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        # print(data)
        return '%s: %s, %s' % (city, data['low'], data['high'])

    # 迭代器对象需要实现next接口, 需要返回一个城市基本信息,全部迭代完成时候需要抛出异常
    def __next__(self):
        # 如果全部迭代完成
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


# 使用时候，实例化
# [u'南京', u'上海', u'北京', u'深圳']
for city in WeatherIterable([u'南京', u'上海', u'北京', u'深圳']):
    print(city)

```
![](./img/用例结果.png)
    
这里我们就实现了一个可迭代对象和迭代器对象，并且用示例感受了某些需要惰性访问场景使用他们的优势。


