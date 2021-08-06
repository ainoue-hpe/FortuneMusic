from typing import Text
import requests
import json    
import datetime

#↑モジュール類のインポート
date = datetime.datetime.today().strftime("%Y/%m/%d")  #今日の日付を出してdateに代入

url='http://api.jugemkey.jp/api/horoscope/free/'+ date     #url情報(http://api.jugemkey.jp/api/horoscope/year/month/day の形式)

r = requests.get(url)   #request.getを使い上記のレスポンス内容を変数に保管

res=json.loads(r.text)  #JSON文字列を辞書に変換

point=r.json()["horoscope"][date]  #pointにr.json()["horoscope"][date]を代入

point_list=[]   #point_listという空のリストを定義
point_dict={}   #point_dictというからのdictを定義



for i in range(len(point)):   #pointのリストの項目の数繰り返す

    #print用(わかりやすく表示用)
    #print('星座 : ',point[i]['sign'])
    #print('本日のワンポイントアドバイス : ',point[i]['content'])  
    #print('本日の総合順位 : ',point[i]['total'])
    #print('本日の金運順位 : ',point[i]['money'])　　　　　　#print用(なんとなくの表示用)

    point_list.append(point[i]['sign'])   #point_listに星座名を追記（牡羊座から順に）

    point_dict[i]=point[i]   #point_dictに星座名ごとの情報を追記（牡羊座から順に）
   
    point_dict[point_list[i]]=point_dict.pop(i)   #辞書型のkeyが数字のままなので対応している星座名に変換



#print(point_list)   #リストの中の星座名を表示

#print(json.dumps(point_dict, indent=4, ensure_ascii=False))   #point_dictをJSON文字列として整形して出力

print(point_dict['双子座'])  #key名（星座名）の指定で情報を取り出す（例：双子座）
print(point_dict['双子座']['content'])  #key名（星座名）（要素名）の指定で情報を取り出す（例：双子座のcontentsを出したいとき）





def return_text(data):
    hoge=json.dumps(point_dict[data], indent=4, ensure_ascii=False)
    return hoge