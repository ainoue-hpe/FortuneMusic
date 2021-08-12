import requests
import json
import datetime

import os
#08/05

date = datetime.datetime.today().strftime("%Y/%m/%d")

# http://api.jugemkey.jp/api/horoscope/year/month/day の形式
res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ date)

#print(json.dumps(json.loads(res.text), indent=4, ensure_ascii=False))
    
#たとえば、牡羊座のみ取得したい場合
#print(res.json()["horoscope"][date][0])

# 以下を追記(return_text()を呼び出すと"Hello!!"が返される)        
#def return_text():
   # return (res.json()["horoscope"][date][0])

point_dict =  (res.json()["horoscope"][date])  

