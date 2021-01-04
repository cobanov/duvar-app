import json


def entryContentCheck(content):
    """ """
    if content == "" or content == " ":
        return False

    return True


def entryFilter(content):
    """ """
    content = content.split(" ")
    with open("app/wordBlacklist.txt", "r", encoding="utf-8") as file:
        bad_words_list = file.read().splitlines()
        clean_content = []
    
        for word in content:
            word = ''.join([i for i in word if not i.isdigit()]) 
            if word in bad_words_list:
                word = len(word) * '*'
                clean_content.append(word)
            else:
                clean_content.append(word)

        clean_content_str = " ".join(clean_content)
    return clean_content_str
