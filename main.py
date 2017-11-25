# web scraper to help find good jobs

# TODO: Get list of training data (20 great jobs and 20 bad jobs).
# TODO: Scrape them and store word frequency in separate hash maps.

import requests
from bs4 import BeautifulSoup
from os import getcwd as cwd
import re
import string


# file paths
target_path = cwd() + "target.txt"
ut = ["script", "style", "head"]
target = target_path + "output_dict.txt"
good_jobs_file = cwd() + "/job_postings/good_jobs.txt"

# data storage
bad_dict = {}
good_dict = {}
good_jobs = []


def get_urls(filepath, url_list):
    # return a list of job posting URLs or filepaths
    with open(filepath, 'r') as f:
        for line in f:
            # standardize this to work for local files, too
            # -1 to get rid of \n char. -2 to get rid of " and \n
            end = len(line) - 2  # compensate for linebreak and quotation
            start = line.index("http")
            url = line[start:end]
            url_list.append(url)
    return url_list


def get_page(url, online=True):
    # can get online or offline HTML files
    if online:
        html = requests.get(url).text
    else:
        html = open(url, 'r', encoding="UTF-8").read()
    return html


def get_text(soup, unwanted_tags):
    word_list = []
    tags_list = soup.find_all("body")
    for tag in tags_list:
        # TODO: This is not skipping all unwanted tags
        if tag.name in unwanted_tags:
            continue
        words = tag.text.split(" ")
        for word in words:
            # TODO: clean word param to have no punctuation before passing in
            if valid_word(word):
                # Normalize the words before adding them to improve comparisons
                word_list.append(word.lower())
    return word_list


def valid_word(word):
    max_length = 20
    word_len = len(word)
    if word_len < 1:
        return False
    if word[0] in string.punctuation:
        return False
    #for char in word:
    #    if char in string.punctuation:
    #        pass #return False
    return word_len < max_length


def add_to_dict(word, word_dict):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    return word_dict


def build_dict(hash_table, word_list):
    for w in word_list:
        add_to_dict(w, hash_table)
    return hash_table


def make_soup(page):
    # TODO: If you can process this to remove all <script> and <style> tags,
    # TODO: Your return value will be easier to work with.
    soup = BeautifulSoup(page, "html.parser")
    return soup


def scrape_page(url, frequency_dict):
    page = get_page(url)
    s = make_soup(page)
    frequent_words = get_text(s, ut)
    w_dict = build_dict(frequency_dict, frequent_words)
    # TODO: refactor so this doesn't need to be resorted for each page
    frequencies = sorted(w_dict.items(), key=lambda x: x[1], reverse=True)
    return frequencies


def write_to_file(frequencies, target_file):
    with open(target_file, 'w', encoding='UTF-8') as file:
        counter = 1
        for fw in frequencies:
            file.write(str(counter) + " " + str(fw) + "\n")
            counter += 1


def main():
    job_list = get_urls(good_jobs_file, good_jobs)
    for j in job_list:
        good_words = scrape_page(j, good_dict)
    write_to_file(good_words, target)


if __name__ == '__main__':
    main()
    # get_urls(cwd() + "/job_postings/good_jobs.txt", good_jobs)


