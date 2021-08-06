import json
# import Spotify
import fortune_json

# with open('fortuneresult.json', encoding='utf-8') as f:
#     jsn = json.load(f)

    # for a in jsn['牡羊座']:
    # print(jsn.get("牡羊座").get("total"))
    # total = jsn.get("牡羊座").get("total")
    # money = jsn.get("牡羊座").get("money")
    # print(jsn.get("牡羊座").get("money"))

max_val = 0
element = ''
sign = '山羊座'

if fortune_json.point_dict[sign]['total'] > max_val:
    max_val = fortune_json.point_dict[sign]['total']
    element = 'valence'
    if fortune_json.point_dict[sign]['job'] > max_val:
        max_val = fortune_json.point_dict[sign]['job']
        element = 'energy'
        if fortune_json.point_dict[sign]['money'] > max_val:
            max_val = fortune_json.point_dict[sign]['money']
            element = 'danceability'
            if fortune_json.point_dict[sign]['love'] > max_val:
                max_val = fortune_json.point_dict[sign]['love']
                element = 'acousticness'

print(element)