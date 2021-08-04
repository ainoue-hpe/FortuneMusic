import json

# def helloworld():
#     name = input('input your name: ')
#     message = 'Hello ' + name + ' !'
#     print(message)

# helloworld()

def main():
    f = open('fortuneresult.json','r',encoding='utf-8')

    jsn = json.load(f)

# with open('fortuneresult.json', encoding='utf-8') as f:
#     jsn = json.load(f)

    # for a in jsn['牡羊座']:
    print(jsn.get("牡羊座").get("total"))
    total = jsn.get("牡羊座").get("total")
    # if total > 4:

    # print("{}".format(json.dumps(jsn,indent=2)))

if __name__=='__main__':
    main()