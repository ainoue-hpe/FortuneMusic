# coding:utf-8
import os
import csv


# htmlからのデータをcsvファイルに記録
def write_csv(data):
    datas = [data]
    with open(os.getcwd()+'/FortuneMusic_App/application/'+'data.csv','a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(datas)


   # 以下を追記(return_text()を呼び出すと"Hello!!"が返される)        
def return_text(data):
    return "Hello!!"+data

