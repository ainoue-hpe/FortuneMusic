import json
import Test_Fortune
from Test_Fortune import Fortune_dict
# import Spotify


#print(Fortune_dict)

# with open('fortuneresult.json', encoding='utf-8') as f:
#     jsn = json.load(f)

    # for a in jsn['牡羊座']:
    # print(jsn.get("牡羊座").get("total"))
    # total = jsn.get("牡羊座").get("total")
    # money = jsn.get("牡羊座").get("money")
    # print(jsn.get("牡羊座").get("money"))


def hikaku(data):
    max_val = 0
    element = ''
    sign=data
    if Test_Fortune.Fortune_dict[sign]['total'] > max_val:
        max_val = Test_Fortune.Fortune_dict[sign]['total']
        element = 'valence'
        if Test_Fortune.Fortune_dict[sign]['job'] > max_val:
            max_val = Test_Fortune.Fortune_dict[sign]['job']
            element = 'energy'
        elif Test_Fortune.Fortune_dict[sign]['money'] > max_val:
            max_val = Test_Fortune.Fortune_dict[sign]['money']
            element = 'danceability'
        elif Test_Fortune.Fortune_dict[sign]['love'] > max_val:
            max_val = Test_Fortune.Fortune_dict[sign]['love']
            element = 'acousticness'

    item=element
    #print("element:"+element)
    return element

data=hikaku("牡羊座")
data_1=hikaku("蟹座")
data_2=hikaku("乙女座")
data_3=hikaku("射手座")
data_4=hikaku("山羊座")



print("牡羊座"+data)
print("蟹座"+data_1)
print("乙女座"+data_2)
print("射手座"+data_3)
print("山羊座"+data_4)
    
