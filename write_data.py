import os

   # htmlからのデータをcsvファイルに記録
def fortune_csv(data):
    datas = [data]
    with open(os.getcwd()+'/group5app/applicationfortune/'+'data.csv','a') as f:
        writer = data.csv.writer(f, lineterminator='\n')
        writer.writerow(datas)