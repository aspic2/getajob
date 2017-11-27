# web scraper to help find good jobs

# TODO: Get list of training data (20 great jobs and 20 bad jobs).
# TODO: Scrape them and store word frequency in separate hash maps.

import requests
from bs4 import BeautifulSoup
from os import getcwd as cwd
import string
import re


# file paths
ut = ["script", "style", "head"]
gj_target = cwd() + "/gj.txt"
bj_target = cwd() + "/bj.txt"
good_jobs_file = cwd() + "/job_postings/good_jobs.txt"
bad_jobs_file = cwd() + "/job_postings/bad_jobs.txt"
offline_jobs_file = cwd() + "/job_postings/offline_jobs.txt"

# data storage
bad_dict = {}
bad_jobs = []
good_dict = {}
good_jobs = []
punctuation = re.compile("\W")


class JobsData(object):
    """Store the dict and the list together in this object."""

    def __init__(self, name, good=True):
        self.j_dict = {}
        self.j_list = []

    def sort_list(self):
        self.j_list = sorted(self.j_dict.items(), key=lambda x: x[1], reverse=True)
        return self


def get_urls(filepath, url_list, online=True):
    # return a list of job posting URLs or filepaths
    with open(filepath, 'r') as f:
        for line in f:
            # TODO: standardize this to work for local files, too
            end = len(line) - 2  # compensate for linebreak and quotation
            # compensate for local files
            if online:
                start = line.index("http")
            else:
                start = line.index("C:")
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


def get_text(soup, unwanted_tags, regex):
    """Should clean up the source HTML to return only displayed text.
    Currently not fully removing CSS and Script data"""
    word_list = []
    tags_list = soup.find_all("body")
    for tag in tags_list:
        # TODO: This is not skipping all unwanted tags
        if tag.name in unwanted_tags:
            continue
        words = regex.split(tag.text)
        for w in words:
            if valid_word(w):
                word_list.append(w.lower())
    return word_list


def valid_word(word):
    min_length = 1
    max_length = 20
    word_len = len(word)
    return min_length < word_len < max_length


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


def scrape_page(url, frequency_dict, online=True):
    page = get_page(url, online)
    s = make_soup(page)
    frequent_words = get_text(s, ut, punctuation)
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


def main(online=True):
    gj = create_word_sets(good_jobs_file, good_jobs, good_dict, gj_target)
    bj = create_word_sets(bad_jobs_file, bad_jobs, bad_dict, bj_target)
    unique_good_words = (set(x[0] for x in gj) - set(x[0] for x in bj))
    write_to_file(unique_good_words, cwd() + "/unique_good_words.txt")


def create_word_sets(file, word_list, dictionary, new_file, online=True):
    # job_list = get_urls(good_jobs_file, good_jobs)
    job_list = get_urls(file, word_list, online)
    for j in job_list:
        word_list = scrape_page(j, dictionary, online)
    write_to_file(word_list, new_file)
    return word_list


if __name__ == '__main__':
    main(online=False)
    # get_urls(cwd() + "/job_postings/good_jobs.txt", good_jobs)


