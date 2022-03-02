import json
import re


REGEX_FOR_TEL_NUMBER = r'(\+9)?0?(\ |-|\()*[0-9]{3}(\ |-|\))*[0-9]{3}[ -]*[0-9]{2}[ -]*[0-9]{2}'
REGEX_FOR_URL = r'https?:\/\/[\w/\-?=%.]+\.[\w/\-&?=%.]+'


def regex_filter(text, regex, replace_with=" ***** "):
    """ String içerisinde regex'e uyan tüm örnekleri bulur.
    replace_with değişkeni ile değiştirir."""
    return re.sub(regex, replace_with, text)


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
            if word in bad_words_list:
                word = len(word) * '*'
                clean_content.append(word)
            else:
                clean_content.append(word)

        clean_content_str = " ".join(clean_content)

    # clean tel-number.
    clean_content_str = regex_filter(text=clean_content_str,
                                     regex=REGEX_FOR_TEL_NUMBER)
    # clean url.
    clean_content_str = regex_filter(text=clean_content_str,
                                     regex=REGEX_FOR_URL)

    return clean_content_str
