from FortuneMusic_App import Fortune_json, branch
from django.shortcuts import render
import sys
import os
import json

from django.http import HttpResponse
from . import Fortune_Spotify

# Create your views here.
# 以下を追記
def index(req):
    myapp_data={
      "insert": Fortune_json.point_list
    }
    return render(req, 'index.html',myapp_data)

    # ajaxでurl指定したメソッド
def call_file(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        #branch.hikaku(req.GET.get("seiza"))  
        
        # write_data.pyの中に新たに記述したメソッド(return_text())を呼び出す。
        #data=Fortune_json.Fortune_dict
        file = json.dumps(Fortune_Spotify.judge(req.GET.get("seiza")),indent=4, ensure_ascii=False)      
          # 受け取ったデータをhtmlに渡す。
        return HttpResponse(file)

