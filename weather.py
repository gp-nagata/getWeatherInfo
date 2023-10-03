import requests
from bs4 import BeautifulSoup

def GetYahooWeather(AreaCode):
    """
    Yahoo天気予報をスクレイピングする関数。

    Parameters
    ----------
    AreaCode : int
        対象となる地域コードを指定。
    
    Returns
    -------
    str
        対象地域の今日と明日の天気予報を返す。
    """
    url = "https://weather.yahoo.co.jp/weather/jp/13/" + str(AreaCode) + ".html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    weather_info = soup.find(class_='forecastCity')
    weather_info = [i.strip() for i in weather_info.text.splitlines()]
    weather_info = [i for i in weather_info if i != ""]
    today = weather_info[0] # 今日の日付
    today_weather = weather_info[1] # 今日の天気
    tomorrow = weather_info[19] # 明日の日付
    tomorrow_weather = weather_info[20] # 明日の天気
    return f"{today}の天気は{today_weather}、{tomorrow}の天気は{tomorrow_weather}です。"

print(GetYahooWeather(4410))
