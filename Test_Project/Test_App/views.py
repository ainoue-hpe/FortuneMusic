from django.shortcuts import render
from django.http import HttpResponse
# application/FortuneMusic_json.pyをインポートする
import FortuneMusic_json
import Unit



  # Create your views here.
def index(req):
      return render(req, 'index.html')

  # ajaxでurl指定したメソッド
def call_write_data(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csvメソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        FortuneMusic_json.return_text(req.GET.get("input_data"))

        file = FortuneMusic_json.return_text()
          # 受け取ったデータをhtmlに渡す。
        return HttpResponse(file)
