import requests
from bs4 import BeautifulSoup

def GetYahooWeather(AreaCode):

    # Yahoo天気情報のURLを生成
    url = "https://weather.yahoo.co.jp/weather/jp/13/" + str(AreaCode) + ".html"

    # URLにアクセスしてHTMLを取得
    r = requests.get(url)

    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(r.text, 'html.parser')

    # 天気情報を含むHTML要素を取得
    weather_info = soup.find(class_='forecastCity')

    # 改行文字を基準にテキストを分割してリストに格納
    weather_info = [i.strip() for i in weather_info.text.splitlines()]

    # 空の要素を削除
    weather_info = [i for i in weather_info if i != ""]

    # 今日の日付を取得
    today = weather_info[0]

    # 今日の天気を取得
    today_weather = weather_info[1]

    # 明日の日付を取得
    tomorrow = weather_info[19]

    # 明日の天気を取得
    tomorrow_weather = weather_info[20]

    # 天気情報を文字列として返す
    return f"{today}の天気は{today_weather}、{tomorrow}の天気は{tomorrow_weather}です。"

# 関数を呼び出して天気情報を取得し、表示
print(GetYahooWeather(4410))
