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

if fortune_json.point_dict['牡羊座']['total'] > max_val:
    max_val = fortune_json.point_dict['牡羊座']['total']
    element = 'valence'
elif fortune_json.point_dict['牡羊座']['job'] > max_val:
    max_val = fortune_json.point_dict['牡羊座']['job']
    element = 'energy'
elif fortune_json.point_dict['牡羊座']['money'] > max_val:
    max_val = fortune_json.point_dict['牡羊座']['money']
    element = 'danceability'
else:
    max_val = fortune_json.point_dict['牡羊座']['love']
    element = 'acousticness'

print(element)