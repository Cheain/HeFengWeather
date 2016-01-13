# IDE : PyCharm Community Edition 5.0.3
# Development language : Python 3.5.1
# If you want to use this program ,please apply a new key for yourself and use your own key
# You can see all the weather information in 'allWeatherInfo' , and choose which you need to show
# What I showed is in the 'weatherForrcast' and packaging for some functions
# The description of the weather I used Chinese , if you want to query the other country please alter the dercription
import json
import urllib.parse
import urllib.request

import weatherForecast

city = urllib.parse.quote(input('输入您要查询的城市名、拼音或英文：'))  # change Chinese string to URL code
myKey = 'cb7d5850fce846e0933dd93826b2da98'
url = 'https://api.heweather.com/x3/weather?city=%s&key=%s' % (city, myKey)
req = urllib.request.urlopen(url)
content = req.read()
if (content):
    content = json.loads(content.decode(encoding='utf-8'))  # decode JSON string to dict
    print('------------------------------------------------------------------------------')
    weatherForecast.status(content)
    weatherForecast.basic(content)
    weatherForecast.air(content)
    weatherForecast.now(content)
    weatherForecast.suggestion(content)
    weatherForecast.hourlyForecast(content)
    weatherForecast.dailyForecast(content)
