import json
import FortuneMusic_json
# import Spotify

# with open('fortuneresult.json', encoding='utf-8') as f:
#     jsn = json.load(f)

    # for a in jsn['牡羊座']:
    # print(jsn.get("牡羊座").get("total"))
    # total = jsn.get("牡羊座").get("total")
    # money = jsn.get("牡羊座").get("money")
    # print(jsn.get("牡羊座").get("money"))


def return_text(data):
    max_val = 0
    element = ''
    sign=data
    if FortuneMusic_json.point_dict[sign]['total'] > max_val:
        max_val = FortuneMusic_json.point_dict[sign]['total']
        element = 'valence'
        if FortuneMusic_json.point_dict[sign]['job'] > max_val:
            max_val = FortuneMusic_json.point_dict[sign]['job']
            element = 'energy'
            if FortuneMusic_json.point_dict[sign]['money'] > max_val:
                max_val = FortuneMusic_json.point_dict[sign]['money']
                element = 'danceability'
                if FortuneMusic_json.point_dict[sign]['love'] > max_val:
                    max_val = FortuneMusic_json.point_dict[sign]['love']
                    element = 'acousticness'

    #print(element)


    return element 

