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
#ここから
#おひつじ座○
sheet1=fortune.point_dict[0]["rank"]
sheet2=fortune.point_dict[0]["content"]
sheet3=fortune.point_dict[0]["total"]
sheet4=fortune.point_dict[0]["money"]
sheet5=fortune.point_dict[0]["job"]
sheet6=fortune.point_dict[0]["love"]
sheet7=fortune.point_dict[0]["color"]
sheet8=fortune.point_dict[0]["item"]
#おうし座1○
sheet11=fortune.point_dict[1]["rank"]
sheet12=fortune.point_dict[1]["content"]
sheet13=fortune.point_dict[1]["total"]
sheet14=fortune.point_dict[1]["money"]
sheet15=fortune.point_dict[1]["job"]
sheet16=fortune.point_dict[1]["love"]
sheet17=fortune.point_dict[1]["color"]
sheet18=fortune.point_dict[1]["item"]
#ふたご座2○
sheet21=fortune.point_dict[2]["rank"]
sheet22=fortune.point_dict[2]["content"]
sheet23=fortune.point_dict[2]["total"]
sheet24=fortune.point_dict[2]["money"]
sheet25=fortune.point_dict[2]["job"]
sheet26=fortune.point_dict[2]["love"]
sheet27=fortune.point_dict[2]["color"]
sheet28=fortune.point_dict[2]["item"]
#かに座3○
sheet31=fortune.point_dict[3]["rank"]
sheet32=fortune.point_dict[3]["content"]
sheet33=fortune.point_dict[3]["total"]
sheet34=fortune.point_dict[3]["money"]
sheet35=fortune.point_dict[3]["job"]
sheet36=fortune.point_dict[3]["love"]
sheet37=fortune.point_dict[3]["color"]
sheet38=fortune.point_dict[3]["item"]
#しし座4○
sheet41=fortune.point_dict[4]["rank"]
sheet42=fortune.point_dict[4]["content"]
sheet43=fortune.point_dict[4]["total"]
sheet44=fortune.point_dict[4]["money"]
sheet45=fortune.point_dict[4]["job"]
sheet46=fortune.point_dict[4]["love"]
sheet47=fortune.point_dict[4]["color"]
sheet48=fortune.point_dict[4]["item"]
#おとめ座5○
sheet51=fortune.point_dict[5]["rank"]
sheet52=fortune.point_dict[5]["content"]
sheet53=fortune.point_dict[5]["total"]
sheet54=fortune.point_dict[5]["money"]
sheet55=fortune.point_dict[5]["job"]
sheet56=fortune.point_dict[5]["love"]
sheet57=fortune.point_dict[5]["color"]
sheet58=fortune.point_dict[5]["item"]
#てんびん座6○
sheet61=fortune.point_dict[6]["rank"]
sheet62=fortune.point_dict[6]["content"]
sheet63=fortune.point_dict[6]["total"]
sheet64=fortune.point_dict[6]["money"]
sheet65=fortune.point_dict[6]["job"]
sheet66=fortune.point_dict[6]["love"]
sheet67=fortune.point_dict[6]["color"]
sheet68=fortune.point_dict[6]["item"]
#さそり座7○
sheet71=fortune.point_dict[7]["rank"]
sheet72=fortune.point_dict[7]["content"]
sheet73=fortune.point_dict[7]["total"]
sheet74=fortune.point_dict[7]["money"]
sheet75=fortune.point_dict[7]["job"]
sheet76=fortune.point_dict[7]["love"]
sheet77=fortune.point_dict[7]["color"]
sheet78=fortune.point_dict[7]["item"]
#おひつじ座8○
sheet81=fortune.point_dict[8]["rank"]
sheet82=fortune.point_dict[8]["content"]
sheet83=fortune.point_dict[8]["total"]
sheet84=fortune.point_dict[8]["money"]
sheet85=fortune.point_dict[8]["job"]
sheet86=fortune.point_dict[8]["love"]
sheet87=fortune.point_dict[8]["color"]
sheet88=fortune.point_dict[8]["item"]
#おひつじ座9○
sheet91=fortune.point_dict[9]["rank"]
sheet92=fortune.point_dict[9]["content"]
sheet93=fortune.point_dict[9]["total"]
sheet94=fortune.point_dict[9]["money"]
sheet95=fortune.point_dict[9]["job"]
sheet96=fortune.point_dict[9]["love"]
sheet97=fortune.point_dict[9]["color"]
sheet98=fortune.point_dict[9]["item"]
#おひつじ座10○
sheet101=fortune.point_dict[10]["rank"]
sheet102=fortune.point_dict[10]["content"]
sheet103=fortune.point_dict[10]["total"]
sheet104=fortune.point_dict[10]["money"]
sheet105=fortune.point_dict[10]["job"]
sheet106=fortune.point_dict[10]["love"]
sheet107=fortune.point_dict[10]["color"]
sheet108=fortune.point_dict[10]["item"]
#おひつじ座11○
sheet111=fortune.point_dict[11]["rank"]
sheet112=fortune.point_dict[11]["content"]
sheet113=fortune.point_dict[11]["total"]
sheet114=fortune.point_dict[11]["money"]
sheet115=fortune.point_dict[11]["job"]
sheet116=fortune.point_dict[11]["love"]
sheet117=fortune.point_dict[11]["color"]
sheet118=fortune.point_dict[11]["item"]


def index(req):
    myapp_data = {
        #おひつじ座
    'insert_rank': sheet1,
    'insert_content': sheet2,
    'insert_total': sheet3,
    'insert_money': sheet4,
    'insert_job': sheet5,
    'insert_love': sheet6,
    'insert_color': sheet7,
    'insert_item': sheet8,
        #おうし座
    '1insert_rank': sheet11,
    '1insert_content': sheet12,
    '1insert_total': sheet13,
    '1insert_money': sheet14,
    '1insert_job': sheet15,
    '1insert_love': sheet16,
    '1insert_color': sheet17,
    '1insert_item': sheet18,
        #ふたご座
    '2insert_rank': sheet21,
    '2insert_content': sheet22,
    '2insert_total': sheet23,
    '2insert_money': sheet24,
    '2insert_job': sheet25,
    '2insert_love': sheet26,
    '2insert_color': sheet27,
    '2insert_item': sheet28,
        #かに座
    '3insert_rank': sheet31,
    '3insert_content': sheet32,
    '3insert_total': sheet33,
    '3insert_money': sheet34,
    '3insert_job': sheet35,
    '3insert_love': sheet36,
    '3insert_color': sheet37,
    '3insert_item': sheet38,
        #しし座
    '4insert_rank': sheet41,
    '4insert_content': sheet42,
    '4insert_total': sheet43,
    '4insert_money': sheet44,
    '4insert_job': sheet45,
    '4insert_love': sheet46,
    '4insert_color': sheet47,
    '4insert_item': sheet48,
    #おとめ座
    '5insert_rank': sheet51,
    '5insert_content': sheet52,
    '5insert_total': sheet53,
    '5insert_money': sheet54,
    '5insert_job': sheet55,
    '5insert_love': sheet56,
    '5insert_color': sheet57,
    '5insert_item': sheet58,
    #てんびん座
    '6insert_rank': sheet61,
    '6insert_content': sheet62,
    '6insert_total': sheet63,
    '6insert_money': sheet64,
    '6insert_job': sheet65,
    '6insert_love': sheet66,
    '6insert_color': sheet67,
    '6insert_item': sheet68,
    #さそり座
    '7insert_rank': sheet71,
    '7insert_content': sheet72,
    '7insert_total': sheet73,
    '7insert_money': sheet74,
    '7insert_job': sheet75,
    '7insert_love': sheet76,
    '7insert_color': sheet77,
    '7insert_item': sheet78,
    #いて座
    '8insert_rank': sheet81,
    '8insert_content': sheet82,
    '8insert_total': sheet83,
    '8insert_money': sheet84,
    '8insert_job': sheet85,
    '8insert_love': sheet86,
    '8insert_color': sheet87,
    '8insert_item': sheet88,
    #やぎ座
    '9insert_rank': sheet91,
    '9insert_content': sheet92,
    '9insert_total': sheet93,
    '9insert_money': sheet94,
    '9insert_job': sheet95,
    '9insert_love': sheet96,
    '9insert_color': sheet97,
    '9insert_item': sheet98,
    #みずがめ座
    '10insert_rank': sheet101,
    '10insert_content': sheet102,
    '10insert_total': sheet103,
    '10insert_money': sheet104,
    '10insert_job': sheet105,
    '10insert_love': sheet106,
    '10insert_color': sheet107,
    '10insert_item': sheet108,
    #うお座
    '11insert_rank': sheet111,
    '11insert_content': sheet112,
    '11insert_total': sheet113,
    '11insert_money': sheet114,
    '11insert_job': sheet115,
    '11insert_love': sheet116,
    '11insert_color': sheet117,
    '11insert_item': sheet118,
    }
    return render(req, 'index.html',myapp_data)
