from django.shortcuts import render
from django.http import HttpResponse
# applicationfortune/fortune.pyをインポートする
#import fortune
from . import fortune
#from .applicationfortune import fortune
#from fortune import show
#from .applicationfortune import Request, Response, get_fortune

# Create your views here.
# 以下を追記
def index(req):
    return render(req, 'index.html')

def sub(req):
    # 運勢を取得(API) result = fortune.hoge('oushi')
    #return HttpResponse('あなたの運勢は。。')
    return render(req, 'subpage.html')
  