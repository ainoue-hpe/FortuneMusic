from FortuneMusic_App import branch
from django.shortcuts import render
import sys
import os

from django.http import HttpResponse
from . import Fortune_Spotify

# Create your views here.
# 以下を追記
def index(req):
    return render(req, 'index.html')

    # ajaxでurl指定したメソッド
def call_write_data(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        branch.hikaku(req.GET.get("seiza"))  
        
        # write_data.pyの中に新たに記述したメソッド(return_text())を呼び出す。
        file = Fortune_Spotify.judge(req.GET.get("seiza"))
       
          # 受け取ったデータをhtmlに渡す。
        return HttpResponse(file)