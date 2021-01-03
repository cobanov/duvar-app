import json

def entryContentCheck(content):
    #content = str(content).strip()
    if content == "":
        return False
    return True

def entryFilter(content):
    content = content.split(" ")
    with open("app/wordBlacklist.txt","r",encoding="utf-8") as file:
        swearing_list = file.read().splitlines()
        #print(swearing_list)
        for i in range(len(content)):
            for swearing in swearing_list:
                #print(f"{swearing}, {content[i]}")
                if content[i] == swearing:
                    content[i] = len(swearing) * '*'
    str = ""
    for word in content:
        str += word + " "
    print("filterli : "+str)
    return str