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
