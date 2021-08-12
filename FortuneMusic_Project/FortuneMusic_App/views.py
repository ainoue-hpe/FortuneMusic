from FortuneMusic_App import Fortune_json, branch
from django.shortcuts import render
import sys
import os
import json

from django.http import HttpResponse
from . import Fortune_Spotify

# Create your views here.
# 以下を追記
 
sheet1=Fortune_json.point[0]["rank"]
sheet2=Fortune_json.point[0]["content"]
sheet3=Fortune_json.point[0]["total"]
sheet4=Fortune_json.point[0]["money"]
sheet5=Fortune_json.point[0]["job"]
sheet6=Fortune_json.point[0]["love"]
sheet7=Fortune_json.point[0]["color"]
sheet8=Fortune_json.point[0]["item"]
#sheet9=Spotifyのプレイリストの該当するURLが出るようにする


#おうし座1○
sheet11=Fortune_json.point[1]["rank"]
sheet12=Fortune_json.point[1]["content"]
sheet13=Fortune_json.point[1]["total"]
sheet14=Fortune_json.point[1]["money"] 
sheet15=Fortune_json.point[1]["job"]
sheet16=Fortune_json.point[1]["love"]
sheet17=Fortune_json.point[1]["color"]
sheet18=Fortune_json.point[1]["item"]
#sheet19=#Spotifyのプレイリストの該当するURLが出るようにする


#ふたご座2○
sheet21=Fortune_json.point[2]["rank"]
sheet22=Fortune_json.point[2]["content"]
sheet23=Fortune_json.point[2]["total"]
sheet24=Fortune_json.point[2]["money"]
sheet25=Fortune_json.point[2]["job"]
sheet26=Fortune_json.point[2]["love"]
sheet27=Fortune_json.point[2]["color"]
sheet28=Fortune_json.point[2]["item"]
#sheet29=Spotifyのプレイリストの該当するURLが出るようにする


#かに座3○
sheet31=Fortune_json.point[3]["rank"]
sheet32=Fortune_json.point[3]["content"]
sheet33=Fortune_json.point[3]["total"]
sheet34=Fortune_json.point[3]["money"]
sheet35=Fortune_json.point[3]["job"]
sheet36=Fortune_json.point[3]["love"]
sheet37=Fortune_json.point[3]["color"]
sheet38=Fortune_json.point[3]["item"]
#sheet39=Spotifyのプレイリストの該当するURLが出るようにする


#しし座4○
sheet41=Fortune_json.point[4]["rank"]
sheet42=Fortune_json.point[4]["content"]
sheet43=Fortune_json.point[4]["total"]
sheet44=Fortune_json.point[4]["money"]
sheet45=Fortune_json.point[4]["job"]
sheet46=Fortune_json.point[4]["love"]
sheet47=Fortune_json.point[4]["color"]
sheet48=Fortune_json.point[4]["item"]
#sheet49=Spotifyのプレイリストの該当するURLが出るようにする


#おとめ座5○
sheet51=Fortune_json.point[5]["rank"]
sheet52=Fortune_json.point[5]["content"]
sheet53=Fortune_json.point[5]["total"]
sheet54=Fortune_json.point[5]["money"]
sheet55=Fortune_json.point[5]["job"]
sheet56=Fortune_json.point[5]["love"]
sheet57=Fortune_json.point[5]["color"]
sheet58=Fortune_json.point[5]["item"]
#sheet59=Spotifyのプレイリストの該当するURLが出るようにする


#てんびん座6○
sheet61=Fortune_json.point[6]["rank"]
sheet62=Fortune_json.point[6]["content"]
sheet63=Fortune_json.point[6]["total"]
sheet64=Fortune_json.point[6]["money"]
sheet65=Fortune_json.point[6]["job"]
sheet66=Fortune_json.point[6]["love"]
sheet67=Fortune_json.point[6]["color"]
sheet68=Fortune_json.point[6]["item"]
#sheet69=Spotifyのプレイリストの該当するURLが出るようにする


#さそり座7○
sheet71=Fortune_json.point[7]["rank"]
sheet72=Fortune_json.point[7]["content"]
sheet73=Fortune_json.point[7]["total"]
sheet74=Fortune_json.point[7]["money"]
sheet75=Fortune_json.point[7]["job"]
sheet76=Fortune_json.point[7]["love"]
sheet77=Fortune_json.point[7]["color"]
sheet78=Fortune_json.point[7]["item"]
#sheet79=Spotifyのプレイリストの該当するURLが出るようにする


#おひつじ座8○
sheet81=Fortune_json.point[8]["rank"]
sheet82=Fortune_json.point[8]["content"]
sheet83=Fortune_json.point[8]["total"]
sheet84=Fortune_json.point[8]["money"]
sheet85=Fortune_json.point[8]["job"]
sheet86=Fortune_json.point[8]["love"]
sheet87=Fortune_json.point[8]["color"]
sheet88=Fortune_json.point[8]["item"]
#sheet89=Spotifyのプレイリストの該当するURLが出るようにする


#おひつじ座9○
sheet91=Fortune_json.point[9]["rank"]
sheet92=Fortune_json.point[9]["content"]
sheet93=Fortune_json.point[9]["total"]
sheet94=Fortune_json.point[9]["money"]
sheet95=Fortune_json.point[9]["job"]
sheet96=Fortune_json.point[9]["love"]
sheet97=Fortune_json.point[9]["color"]
sheet98=Fortune_json.point[9]["item"]
#sheet99=Spotifyのプレイリストの該当するURLが出るようにする


#おひつじ座10○
sheet101=Fortune_json.point[10]["rank"]
sheet102=Fortune_json.point[10]["content"]
sheet103=Fortune_json.point[10]["total"]
sheet104=Fortune_json.point[10]["money"]
sheet105=Fortune_json.point[10]["job"]
sheet106=Fortune_json.point[10]["love"]
sheet107=Fortune_json.point[10]["color"]
sheet108=Fortune_json.point[10]["item"]
#sheet109=Spotifyのプレイリストの該当するURLが出るようにする


#おひつじ座11○
sheet111=Fortune_json.point[11]["rank"]
sheet112=Fortune_json.point[11]["content"]
sheet113=Fortune_json.point[11]["total"]
sheet114=Fortune_json.point[11]["money"]
sheet115=Fortune_json.point[11]["job"]
sheet116=Fortune_json.point[11]["love"]
sheet117=Fortune_json.point[11]["color"]
sheet118=Fortune_json.point[11]["item"]
#sheet119=Spotifyのプレイリストの該当するURLが出るようにする


def index(req):
    myapp_data={

          #おひつじ座
      'insert_rank': sheet1,
      'insert_content': sheet2,
      'insert_total': sheet3,
      'insert_money': sheet4,
      'insert_job': sheet5,
      'insert_love': sheet6,
      'insert_color': sheet7,
      'insert_item': sheet8,
      #'insert_song_playlist': sheet9,


          #おうし座
      '1insert_rank': sheet11,
      '1insert_content': sheet12,
      '1insert_total': sheet13,
      '1insert_money': sheet14,
      '1insert_job': sheet15,
      '1insert_love': sheet16,
      '1insert_color': sheet17,
      '1insert_item': sheet18,
      #'1insert_song_playlist': sheet19,


          #ふたご座
      '2insert_rank': sheet21,
      '2insert_content': sheet22,
      '2insert_total': sheet23,
      '2insert_money': sheet24,
      '2insert_job': sheet25,
      '2insert_love': sheet26,
      '2insert_color': sheet27,
      '2insert_item': sheet28,
      #'2insert_song_playlist': sheet29,


          #かに座
      '3insert_rank': sheet31,
      '3insert_content': sheet32,
      '3insert_total': sheet33,
      '3insert_money': sheet34,
      '3insert_job': sheet35,
      '3insert_love': sheet36,
      '3insert_color': sheet37,
      '3insert_item': sheet38,
      #'3insert_song_playlist': sheet39,


          #しし座
      '4insert_rank': sheet41,
      '4insert_content': sheet42,
      '4insert_total': sheet43,
      '4insert_money': sheet44,
      '4insert_job': sheet45,
      '4insert_love': sheet46,
      '4insert_color': sheet47,
      '4insert_item': sheet48,
      #'4insert_song_playlist': sheet49,


      #おとめ座
      '5insert_rank': sheet51,
      '5insert_content': sheet52,
      '5insert_total': sheet53,
      '5insert_money': sheet54,
      '5insert_job': sheet55,
      '5insert_love': sheet56,
      '5insert_color': sheet57,
      '5insert_item': sheet58,
      #'5insert_song_playlist': sheet59,


      #てんびん座
      '6insert_rank': sheet61,
      '6insert_content': sheet62,
      '6insert_total': sheet63,
      '6insert_money': sheet64,
      '6insert_job': sheet65,
      '6insert_love': sheet66,
      '6insert_color': sheet67,
      '6insert_item': sheet68,
      #'6insert_song_playlist': sheet69,


      #さそり座
      '7insert_rank': sheet71,
      '7insert_content': sheet72,
      '7insert_total': sheet73,
      '7insert_money': sheet74,
      '7insert_job': sheet75,
      '7insert_love': sheet76,
      '7insert_color': sheet77,
      '7insert_item': sheet78,
      #'7insert_song_playlist': sheet79,


      #いて座
      '8insert_rank': sheet81,
      '8insert_content': sheet82,
      '8insert_total': sheet83,
      '8insert_money': sheet84,
      '8insert_job': sheet85,
      '8insert_love': sheet86,
      '8insert_color': sheet87,
      '8insert_item': sheet88,
      #'8insert_song_playlist': sheet89,


      #やぎ座
      '9insert_rank': sheet91,
      '9insert_content': sheet92,
      '9insert_total': sheet93,
      '9insert_money': sheet94,
      '9insert_job': sheet95,
      '9insert_love': sheet96,
      '9insert_color': sheet97,
      '9insert_item': sheet98,
      #'9insert_song_playlist': sheet99,


      #みずがめ座
      '10insert_rank': sheet101,
      '10insert_content': sheet102,
      '10insert_total': sheet103,
      '10insert_money': sheet104,
      '10insert_job': sheet105,
      '10insert_love': sheet106,
      '10insert_color': sheet107,
      '10insert_item': sheet108,
      #'10insert_song_playlist': sheet109,


      #うお座
      '11insert_rank': sheet111,
      '11insert_content': sheet112,
      '11insert_total': sheet113,
      '11insert_money': sheet114,
      '11insert_job': sheet115,
      '11insert_love': sheet116,
      '11insert_color': sheet117,
      '11insert_item': sheet118,
      #'11insert_song_playlist': sheet119,


      
      }
    return render(req, 'index.html',myapp_data)


    # ajaxでurl指定したメソッド
def call_file(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        #branch.hikaku(req.GET.get("seiza"))  
        
        # write_data.pyの中に新たに記述したメソッド(return_text())を呼び出す。
        #data=Fortune_json_json.Fortune_json_dict
        file = json.dumps(Fortune_Spotify.judge(req.GET.get("seiza")),indent=4, ensure_ascii=False)      
          # 受け取ったデータをhtmlに渡す。
        return HttpResponse(file)



