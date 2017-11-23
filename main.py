# web scraper to help find good jobs

# TODO: Get list of training data (20 great jobs and 20 bad jobs).
# TODO: Scrape them and store word frequency in separate hash maps.

import requests
from bs4 import BeautifulSoup
from os import getcwd as cwd
import re
import string


avant = "https://jobs.lever.co/avant/1c9e827f-19da-49ea-91cd-cce64aea0b56"
offline_avant = "C:/Users/mthom/dvStuff/getajob/offline_html/Avant - Software Engineer.html"
target_path = "C:/Users/mthom/dvStuff/getajob/"  # cwd() + "target.txt"
ut = ["script", "style", "head"]


def get_page(url, online=True):
    # can get online or offline HTML files
    if online:
        html = requests.get(url).text
    else:
        html = open(url, 'r', encoding="UTF-8").read()
    return html


def get_text(soup, unwanted_tags):
    word_list = []
    word_length = 25
    tags_list = soup.find_all()
    for tag in tags_list:
        # TODO: This is not skipping all unwanted tags
        if tag.name in unwanted_tags:
            continue
        # TODO: Not working
        if "<script" in tag:
            beginning = tag.index("<script")
            end = tag.index("</script>") + 9
            tag = tag.join(tag[:beginning], tag[end:])
            print(tag)
        if "<style" in tag:
            beginning = tag.index("<style")
            end = tag.index("</style>") + 9
            tag = tag.join(tag[:beginning], tag[end:])
            print(tag)
        #print(tag.name, tag.text)
        words = tag.text.split(" ")
        for word in words:
            if valid_word(word):
                word_list.append(word)
    return word_list


def valid_word(word):
    max_length = 20
    for char in word:
        if char in string.punctuation:
            return False
    return len(word) < max_length


def add_to_dict(word, word_dict):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    return word_dict


def build_dict(word_list):
    d = {}
    for w in word_list:
        add_to_dict(w, d)
    return d


def make_soup(page):
    # TODO: If you can process this to remove all <script> and <style> tags,
    # TODO: Your return value will be easier to work with.
    soup = BeautifulSoup(page, "html5lib")
    return soup


if __name__ == '__main__':
    target_file = target_path + "output_dict.txt"
    page = get_page(offline_avant, False)
    s = make_soup(page)
    frequent_words = get_text(s, ut)
    frequencies = list(build_dict(frequent_words).items())
    frequencies.sort(key=lambda x: x[1], reverse=True)
    with open(target_file, 'w', encoding='UTF-8') as file:
        #for fw in frequent_words:
        file.write(str(frequencies))


