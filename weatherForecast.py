# packaging for some functions to show the weather

# basic
def basic(info):
    try:
        info['HeWeather data service 3.0'][0]['basic']
    except Exception as e:
        pass
    else:
        cityName = info['HeWeather data service 3.0'][0]['basic']['city']  # city name
        countryName = info['HeWeather data service 3.0'][0]['basic']['cnty']  # country name
        localTime = info['HeWeather data service 3.0'][0]['basic']['update']['loc']  # local update time
        print('%s %s,当地%s更新' % (countryName, cityName, localTime))


# air quality index
def air(info):
    try:
        info['HeWeather data service 3.0'][0]['aqi']['city']
    except Exception as e:
        pass
    else:
        aqi = info['HeWeather data service 3.0'][0]['aqi']['city']['aqi']  # air quality index
        pm25 = info['HeWeather data service 3.0'][0]['aqi']['city']['pm25']  # pm2.5 one hour average (ug/m³)
        airQualityType = info['HeWeather data service 3.0'][0]['aqi']['city']['qlty']  # air quality type
        print('空气质量指数%s，pm2.5含量%sug/m³，空气质量%s' % (aqi, pm25, airQualityType))


# live suggestion
def suggestion(info):
    try:
        info['HeWeather data service 3.0'][0]['suggestion']
    except Exception as e:
        pass
    else:
        comfTxt = info['HeWeather data service 3.0'][0]['suggestion']['comf']['txt']  # comfortable details
        dressTxt = info['HeWeather data service 3.0'][0]['suggestion']['drsg']['txt']  # dress details
        uvTxt = info['HeWeather data service 3.0'][0]['suggestion']['uv']['txt']  # ultraviolet ray details
        cwTxt = info['HeWeather data service 3.0'][0]['suggestion']['cw']['txt']  # car wash details
        travelTxt = info['HeWeather data service 3.0'][0]['suggestion']['trav']['txt']  # travel details
        influenzaTxt = info['HeWeather data service 3.0'][0]['suggestion']['flu']['txt']  # influenza details
        sportTxt = info['HeWeather data service 3.0'][0]['suggestion']['sport']['txt']  # sport details
        print('\t%s\n\t%s\n\t%s\n\t%s\n\t%s\n\t%s\n\t%s'
              % (comfTxt, uvTxt, dressTxt, influenzaTxt, sportTxt, cwTxt, travelTxt))


# now the weather
def now(info):
    try:
        info['HeWeather data service 3.0'][0]['now']
    except Exception as e:
        pass
    else:
        temperatureNow = info['HeWeather data service 3.0'][0]['now']['tmp']  # now temperature (℃)
        temperatureFeelNow = info['HeWeather data service 3.0'][0]['now']['fl']  # feel temperature
        windLevelNow = info['HeWeather data service 3.0'][0]['now']['wind']['sc']  # wind level
        windDirectionNow = info['HeWeather data service 3.0'][0]['now']['wind']['dir']  # wind direction
        weatherTxtNow = info['HeWeather data service 3.0'][0]['now']['cond']['txt']  # weather description
        rainFallNow = info['HeWeather data service 3.0'][0]['now']['pcpn']  # rain fall (mm)
        humidityNow = info['HeWeather data service 3.0'][0]['now']['hum']  # humidity (%)
        airPressureNow = info['HeWeather data service 3.0'][0]['now']['pres']  # air pressure
        visibilityNow = info['HeWeather data service 3.0'][0]['now']['vis']  # visibility (Km)
        print('当前气温%s℃，体感%s℃，%s，%s级%s，降雨量%smm，湿度%s%%，气压%shPa，能见度%sKm'
              % (temperatureNow, temperatureFeelNow, weatherTxtNow, windLevelNow, windDirectionNow, rainFallNow,
                 humidityNow,
                 airPressureNow, visibilityNow))


# daily_forecast [1,7]
def dailyForecast(info):
    for i in range(7):
        try:
            info['HeWeather data service 3.0'][0]['daily_forecast'][i]
        except Exception as e:
            pass
        else:
            localDateDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['date']  # local date
            sunriseDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['astro']['sr']  # sunrise time
            sunsetDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['astro']['ss']  # sunset time
            minTemperatureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['tmp'][
                'min']  # min temperature
            maxTemperatureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['tmp'][
                'max']  # max temperature
            windLevelDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['wind']['sc']  # wind level
            windDirectionDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['wind'][
                'dir']  # wind direction
            weatherTxtDayDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['cond'][
                'txt_d']  # weather description
            weatherTxtNightDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['cond'][
                'txt_n']  # weather description
            rainFallDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['pcpn']  # rain fall (mm)
            rainFallProbabilityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i][
                'pop']  # rain fall probability
            humidityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['hum']  # humidity (%)
            airPressureDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['pres']  # air pressure
            visibilityDaily = info['HeWeather data service 3.0'][0]['daily_forecast'][i]['vis']  # visibility (Km)
            print('%s预报：当天日出时间%s，日落时间%s，气温%s~%s℃，%s级%s，白天%s，晚上%s，降雨概率%s%%，'
                  '降雨量%smm，湿度%s%%，气压%shPa，能见度%sKm'
                  % (
                      localDateDaily, sunriseDaily, sunsetDaily, minTemperatureDaily, maxTemperatureDaily,
                      windLevelDaily,
                      windDirectionDaily, weatherTxtDayDaily, weatherTxtNightDaily, rainFallProbabilityDaily,
                      rainFallDaily,
                      humidityDaily, airPressureDaily, visibilityDaily))


# hourly_forecast [1,5]
def hourlyForecast(info):
    for i in range(5):
        try:
            info['HeWeather data service 3.0'][0]['hourly_forecast'][i]
        except Exception as e:
            pass
        else:
            dateTimeHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['date']  # date and time
            temperatureHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['tmp']  # temperature
            windLevelHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['wind']['sc']  # wind level
            windDirectionHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['wind'][
                'dir']  # wind direction
            rainFallProbabilityHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i][
                'pop']  # rain fall probability
            humidityHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['hum']  # humidity (%)
            airPressureHourly = info['HeWeather data service 3.0'][0]['hourly_forecast'][i]['pres']  # air pressure
            print('%s预报：温度%s℃，%s级%s，降雨概率%s%%，湿度%s%%，气压%shPa'
                  % (dateTimeHourly, temperatureHourly, windLevelHourly, windDirectionHourly, rainFallProbabilityHourly,
                     humidityHourly, airPressureHourly))


# error code
states = {'ok': '接口正常', 'invalid key': '错误的用户 key', 'unknown city': '未知城市',
          'no more requests': '超过访问次数', 'anr': '服务无响应或超时', 'permission denied': '没有访问权限'}


def status(info):
    try:
        info['HeWeather data service 3.0'][0]['status']
    except Exception as e:
        pass
    else:
        state = info['HeWeather data service 3.0'][0]['status']  # the state of API
        if state != 'ok':
            print(states[state])
