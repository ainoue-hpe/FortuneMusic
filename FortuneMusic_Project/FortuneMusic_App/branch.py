import json
from FortuneMusic_App import Fortune_json
from FortuneMusic_App.Fortune_json import Fortune_dict
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
    if Fortune_json.Fortune_dict[sign]['total'] > max_val:
        max_val = Fortune_json.Fortune_dict[sign]['total']
        element = 'valence'
        if Fortune_json.Fortune_dict[sign]['job'] > max_val:
            max_val = Fortune_json.Fortune_dict[sign]['job']
            element = 'energy'
        elif Fortune_json.Fortune_dict[sign]['money'] > max_val:
            max_val = Fortune_json.Fortune_dict[sign]['money']
            element = 'danceability'
        elif Fortune_json.Fortune_dict[sign]['love'] > max_val:
            max_val = Fortune_json.Fortune_dict[sign]['love']
            element = 'acousticness'

    item=element
    
    return element
    #print("element:"+element)
