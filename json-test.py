import requests
import json
import datetime


date = datetime.datetime.today().strftime("%Y/%m/%d")

# http://api.jugemkey.jp/api/horoscope/year/month/day の形式
url='http://api.jugemkey.jp/api/horoscope/free/'+ date     #url情報

r = requests.get(url)   #request.getを使いレスポンス内容を変数に保管

res=json.loads(r.text)  #JSON文字列を辞書に変換

print(json.dumps(res, indent=4, ensure_ascii=False))   #辞書をJSON文字列として整形して出力

#print(r.status_code)  #statuscodeの表示

#print(r.text) #json文字列

point=r.json()["horoscope"][date]  #pointにr.json()["horoscope"][date]を代入


#0＝牡羊座の情報を取得#
 #JSONでの名前を指定することで情報がとってこれる

#print(point[0]['sign'])
#print(point[0]['content'])  
#print(point[0]['total'])

#print用
print('星座 : ',point[0]['sign'])
print('本日のワンポイントアドバイス : ',point[0]['content'])  
print('本日の総合順位 : ',point[0]['total'])
print('本日の金運順位 : ',point[0]['money'])
#
