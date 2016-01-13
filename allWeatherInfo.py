# 解析全部返回数据示例

info = {'HeWeather data service 3.0': [{'basic': {'city': '北京', 'cnty': '中国', 'lat': '39.904000',
                                                  'update': {'utc': '2016-01-12 09:04', 'loc': '2016-01-12 17:04'},
                                                  'lon': '116.391000', 'id': 'CN101010100'}, 'status': 'ok',
                                        'suggestion': {
                                            'flu': {'txt': '天气较凉，较易发生感冒，请适当增加衣服。体质较弱的朋友尤其应该注意防护。', 'brf': '较易发'},
                                            'trav': {'txt': '天气较好，同时又有微风伴您一路同行。稍冷，较适宜旅游，您仍可陶醉于大自然的美丽风光中。',
                                                     'brf': '较适宜'},
                                            'sport': {'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。', 'brf': '较不宜'},
                                            'comf': {'txt': '白天天气晴好，但仍会使您感觉偏冷，不很舒适，请注意适时添加衣物，以防感冒。', 'brf': '较不舒适'},
                                            'drsg': {'txt': '天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。',
                                                     'brf': '冷'},
                                            'uv': {'txt': '紫外线强度较弱，建议出门前涂擦SPF在12-15之间、PA+的防晒护肤品。', 'brf': '弱'},
                                            'cw': {'txt': '较适宜洗车，未来一天无雨，风力较小，擦洗一新的汽车至少能保持一天。', 'brf': '较适宜'}},
                                        'hourly_forecast': [{'pres': '1032', 'pop': '0',
                                                             'wind': {'sc': '微风', 'spd': '10', 'deg': '321',
                                                                      'dir': '西北风'}, 'date': '2016-01-12 16:00',
                                                             'hum': '16', 'tmp': '-1'}, {'pres': '1032', 'pop': '0',
                                                                                         'wind': {'sc': '微风',
                                                                                                  'spd': '9',
                                                                                                  'deg': '320',
                                                                                                  'dir': '西北风'},
                                                                                         'date': '2016-01-12 19:00',
                                                                                         'hum': '22', 'tmp': '-3'},
                                                            {'pres': '1032', 'pop': '0',
                                                             'wind': {'sc': '微风', 'spd': '9', 'deg': '325',
                                                                      'dir': '西北风'}, 'date': '2016-01-12 22:00',
                                                             'hum': '26', 'tmp': '-5'}], 'aqi': {
        'city': {'pm10': '34', 'pm25': '10', 'so2': '5', 'o3': '59', 'qlty': '优', 'aqi': '35', 'no2': '17', 'co': '1'}},
                                        'now': {'cond': {'txt': '晴', 'code': '100'}, 'pcpn': '0', 'pres': '1029',
                                                'wind': {'sc': '5-6', 'spd': '27', 'deg': '300', 'dir': '北风'},
                                                'hum': '15', 'vis': '10', 'tmp': '-1', 'fl': '-9'}, 'daily_forecast': [
        {'wind': {'sc': '微风', 'spd': '8', 'deg': '322', 'dir': '无持续风向'},
         'cond': {'txt_n': '晴', 'code_n': '100', 'txt_d': '晴', 'code_d': '100'}, 'pcpn': '0.0', 'pres': '1033',
         'pop': '0', 'astro': {'ss': '17:09', 'sr': '07:35'}, 'date': '2016-01-12', 'hum': '13', 'vis': '10',
         'tmp': {'min': '-8', 'max': '0'}}, {'wind': {'sc': '微风', 'spd': '4', 'deg': '316', 'dir': '无持续风向'},
                                             'cond': {'txt_n': '多云', 'code_n': '101', 'txt_d': '晴', 'code_d': '100'},
                                             'pcpn': '0.0', 'pres': '1026', 'pop': '0',
                                             'astro': {'ss': '17:10', 'sr': '07:34'}, 'date': '2016-01-13', 'hum': '11',
                                             'vis': '10', 'tmp': {'min': '-7', 'max': '2'}},
        {'wind': {'sc': '微风', 'spd': '7', 'deg': '295', 'dir': '无持续风向'},
         'cond': {'txt_n': '晴', 'code_n': '100', 'txt_d': '多云', 'code_d': '101'}, 'pcpn': '0.0', 'pres': '1022',
         'pop': '0', 'astro': {'ss': '17:11', 'sr': '07:34'}, 'date': '2016-01-14', 'hum': '15', 'vis': '10',
         'tmp': {'min': '-7', 'max': '3'}}, {'wind': {'sc': '微风', 'spd': '4', 'deg': '91', 'dir': '无持续风向'},
                                             'cond': {'txt_n': '阴', 'code_n': '104', 'txt_d': '多云', 'code_d': '101'},
                                             'pcpn': '0.0', 'pres': '1021', 'pop': '0',
                                             'astro': {'ss': '17:12', 'sr': '07:34'}, 'date': '2016-01-15', 'hum': '21',
                                             'vis': '10', 'tmp': {'min': '-5', 'max': '2'}},
        {'wind': {'sc': '微风', 'spd': '1', 'deg': '123', 'dir': '无持续风向'},
         'cond': {'txt_n': '阴', 'code_n': '104', 'txt_d': '阴', 'code_d': '104'}, 'pcpn': '1.1', 'pres': '1028',
         'pop': '64', 'astro': {'ss': '17:14', 'sr': '07:33'}, 'date': '2016-01-16', 'hum': '56', 'vis': '10',
         'tmp': {'min': '-7', 'max': '-3'}}, {'wind': {'sc': '微风', 'spd': '3', 'deg': '6', 'dir': '无持续风向'},
                                              'cond': {'txt_n': '阴', 'code_n': '104', 'txt_d': '多云', 'code_d': '101'},
                                              'pcpn': '0.0', 'pres': '1034', 'pop': '27',
                                              'astro': {'ss': '17:15', 'sr': '07:33'}, 'date': '2016-01-17',
                                              'hum': '26', 'vis': '10', 'tmp': {'min': '-8', 'max': '-3'}},
        {'wind': {'sc': '3-4', 'spd': '16', 'deg': '293', 'dir': '北风'},
         'cond': {'txt_n': '晴', 'code_n': '100', 'txt_d': '阴', 'code_d': '104'}, 'pcpn': '0.0', 'pres': '1033',
         'pop': '0', 'astro': {'ss': '17:16', 'sr': '07:33'}, 'date': '2016-01-18', 'hum': '22', 'vis': '10',
         'tmp': {'min': '-8', 'max': '-3'}}]}]}

print(info)  # 接收到的信息例子

# basic
cityName = info['HeWeather data service 3.0'][0]['basic']['city']  # city name
cityID = info['HeWeather data service 3.0'][0]['basic']['id']  # city ID
countryName = info['HeWeather data service 3.0'][0]['basic']['cnty']  # country name
cityLon = info['HeWeather data service 3.0'][0]['basic']['lon']  # city lon
cityLat = info['HeWeather data service 3.0'][0]['basic']['lat']  # city lat
localTime = info['HeWeather data service 3.0'][0]['basic']['update']['loc']  # local update time
UTCTime = info['HeWeather data service 3.0'][0]['basic']['update']['utc']  # UTC update time
print('basic:', cityName, cityID, countryName, cityLon, cityLat, localTime, UTCTime)

# air quality index
aqi = info['HeWeather data service 3.0'][0]['aqi']['city']['aqi']  # air quality index
pm25 = info['HeWeather data service 3.0'][0]['aqi']['city']['pm25']  # pm2.5 one hour average (ug/m³)
pm10 = info['HeWeather data service 3.0'][0]['aqi']['city']['pm10']  # pm10 one hour average (ug/m³)
so2 = info['HeWeather data service 3.0'][0]['aqi']['city']['so2']  # so2 one hour average (ug/m³)
no2 = info['HeWeather data service 3.0'][0]['aqi']['city']['no2']  # no2  one hour average (ug/m³)
co = info['HeWeather data service 3.0'][0]['aqi']['city']['co']  # co  one hour average (ug/m³)
o3 = info['HeWeather data service 3.0'][0]['aqi']['city']['o3']  # o3  one hour average (ug/m³)
airQualityType = info['HeWeather data service 3.0'][0]['aqi']['city']['qlty']  # air quality type
print('aqi:', aqi, pm25, pm10, so2, no2, co, o3, airQualityType)

# live suggestion
comf = info['HeWeather data service 3.0'][0]['suggestion']['comf']['brf']  # comfortable description
comfTxt = info['HeWeather data service 3.0'][0]['suggestion']['comf']['txt']  # comfortable details
dress = info['HeWeather data service 3.0'][0]['suggestion']['drsg']['brf']  # dress description
dressTxt = info['HeWeather data service 3.0'][0]['suggestion']['drsg']['txt']  # dress details
uv = info['HeWeather data service 3.0'][0]['suggestion']['uv']['brf']  # ultraviolet ray description
uvTxt = info['HeWeather data service 3.0'][0]['suggestion']['uv']['txt']  # ultraviolet ray details
cw = info['HeWeather data service 3.0'][0]['suggestion']['cw']['brf']  # car wash description
cwTxt = info['HeWeather data service 3.0'][0]['suggestion']['cw']['txt']  # car wash details
travel = info['HeWeather data service 3.0'][0]['suggestion']['trav']['brf']  # travel description
travelTxt = info['HeWeather data service 3.0'][0]['suggestion']['trav']['txt']  # travel details
influenza = info['HeWeather data service 3.0'][0]['suggestion']['flu']['brf']  # influenza description
influenzaTxt = info['HeWeather data service 3.0'][0]['suggestion']['flu']['txt']  # influenza details
sport = info['HeWeather data service 3.0'][0]['suggestion']['sport']['brf']  # sport description
sportTxt = info['HeWeather data service 3.0'][0]['suggestion']['sport']['txt']  # sport details
print('suggestion:', comf, comfTxt, dress, dressTxt, uv, uvTxt, cw, cwTxt, travel, travelTxt, influenza, influenzaTxt,
      sport, sportTxt)

# now the weather
temperatureNow = info['HeWeather data service 3.0'][0]['now']['tmp']  # now temperature (℃)
temperatureFeelNow = info['HeWeather data service 3.0'][0]['now']['fl']  # feel temperature
windSpeedNow = info['HeWeather data service 3.0'][0]['now']['wind']['spd']  # wind speed (Kmph)
windLevelNow = info['HeWeather data service 3.0'][0]['now']['wind']['sc']  # wind level
windDegreeNow = info['HeWeather data service 3.0'][0]['now']['wind']['deg']  # wind degree
windDirectionNow = info['HeWeather data service 3.0'][0]['now']['wind']['dir']  # wind direction
weatherCodeNow = info['HeWeather data service 3.0'][0]['now']['cond']['code']  # weather code
weatherTxtNow = info['HeWeather data service 3.0'][0]['now']['cond']['txt']  # weather description
rainFallNow = info['HeWeather data service 3.0'][0]['now']['pcpn']  # rain fall (mm)
humidityNow = info['HeWeather data service 3.0'][0]['now']['hum']  # humidity (%)
airPressureNow = info['HeWeather data service 3.0'][0]['now']['pres']  # air pressure
visibilityNow = info['HeWeather data service 3.0'][0]['now']['vis']  # visibility (Km)
print('now:', temperatureNow, temperatureFeelNow, windSpeedNow, windLevelNow, windDegreeNow, windDirectionNow,
      weatherCodeNow, weatherTxtNow, rainFallNow, humidityNow, airPressureNow, visibilityNow)

# daily_forecast [1,7]
localDateDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['date']  # local date
sunriseDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['astro']['sr']  # sunrise time
sunsetDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['astro']['ss']  # sunset time
minTemperatureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['tmp']['min']  # min temperature
maxTemperatureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['tmp']['max']  # max temperature
windSpeedDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['wind']['spd']  # wind speed (Kmph)
windLevelDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['wind']['sc']  # wind level
windDegreeDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['wind']['deg']  # wind degree
windDirectionDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['wind']['dir']  # wind direction
weatherCodeDayDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['cond']['code_d']  # weather code
weatherTxtDayDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['cond']['txt_d']  # weather description
weatherCodeNightDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['cond']['code_n']  # weather code
weatherTxtNightDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['cond'][
    'txt_n']  # weather description
rainFallDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['pcpn']  # rain fall (mm)
rainFallProbabilityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['pop']  # rain fall probability
humidityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['hum']  # humidity (%)
airPressureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['pres']  # air pressure
visibilityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][0]['vis']  # visibility (Km)
print('daily_forecast:', localDateDaily, sunriseDaily, sunsetDaily, minTemperatureDaily, maxTemperatureDaily,
      windSpeedDaily, windLevelDaily, windDegreeDaily, windDirectionDaily, weatherCodeDayDaily, weatherTxtDayDaily,
      weatherCodeNightDaily, weatherTxtNightDaily, rainFallDaily, rainFallProbabilityDaily, humidityDaily,
      airPressureDaily,
      visibilityDaily)

# hourly_forecast [1,5]
dateTimeHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['date']  # date and time
temperatureHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['tmp']  # temperature
windSpeedHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['wind']['spd']  # wind speed (Kmph)
windLevelHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['wind']['sc']  # wind level
windDegreeHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['wind']['deg']  # wind degree
windDirectionHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['wind']['dir']  # wind direction
rainFallProbabilityHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['pop']  # rain fall probability
humidityHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['hum']  # humidity (%)
airPressureHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][0]['pres']  # air pressure
print('hourly_forecast:', dateTimeHourly, temperatureHourly, windSpeedHourly, windLevelHourly, windDegreeHourly,
      windDirectionHourly, rainFallProbabilityHourly, humidityHourly, airPressureHourly)

# error code
status = info['HeWeather data service 3.0'][0]['status']  # the state of API
print('status:', status)
