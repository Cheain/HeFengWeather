import json
import urllib.parse
import urllib.request

import weatherForecast

city = urllib.parse.quote(input('输入您要查询的城市名、拼音或英文：'))  # 将中文字符转为URL编码
url = 'https://api.heweather.com/x3/weather?city=%s&key=cb7d5850fce846e0933dd93826b2da98' % city
req = urllib.request.urlopen(url)
content = req.read()
if (content):
    content = json.loads(content.decode(encoding='utf-8'))  # 将接收到的JSON字符串解码为字典
    print('------------------------------------------------------------------------------')
    weatherForecast.status(content)
    weatherForecast.basic(content)
    weatherForecast.air(content)
    weatherForecast.now(content)
    weatherForecast.suggestion(content)
    weatherForecast.hourlyForecast(content)
    weatherForecast.dailyForecast(content)
