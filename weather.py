import requests
from bs4 import BeautifulSoup

def get_yahoo_weather(area_code):
    # Yahoo天気情報のURLを生成
    url = f"https://weather.yahoo.co.jp/weather/jp/13/{area_code}.html"

    # URLにアクセスしてHTMLを取得。情報を取得するために、どのページから情報元に侵入するか。実際にURLに行き、テキストデータを取得する処理をはじめに書く。
    r = requests.get(url)

    # BeautifulSoupを使ってHTMLを解析よく使うプログラムのかたまりをライブラリと呼ぶが、そのひとつが今回のBeautifulSoup。今回のPythonでは、Webサイトの情報を簡単に取得するために使う。
    soup = BeautifulSoup(r.text, 'html.parser')

    # 天気情報を含むHTML要素を取得
    weather_info = soup.find(class_='forecastCity')

    # テキストを整理
    weather_info_text = [i.strip() for i in weather_info.text.splitlines() if i.strip()]

    # 今日の天気情報と気温を取得
    today_date, today_weather, today_temp = weather_info_text[0], weather_info_text[1], weather_info_text[2]

    # 天気情報と気温を文字列として返す
    return f"{today_date}の天気は{today_weather}、気温は{today_temp}です。"

# 関数を呼び出して天気情報を取得し、表示
print(get_yahoo_weather(4410))
