
def entryContentCheck(content):
    """ """
    if content == "" or content == " ":
        return False

    return True


def entryFilter(content):
    """ """
    content = content.split(" ")
    with open("app/wordBlackList.txt", "r", encoding="utf-8") as file:
        bad_words_list = file.read().splitlines()
        clean_content = []

        for word in content:
            if word in bad_words_list:
                word = word[0] + ((len(word)-1) * '*')
                clean_content.append(word)
            else:
                clean_content.append(word)

        clean_content_str = " ".join(clean_content)
    return clean_content_str
