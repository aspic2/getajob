# web scraper to help find good jobs

# TODO: Get list of training data (20 great jobs and 20 bad jobs).
# TODO: Scrape them and store word frequency in separate hash maps.

import requests
from bs4 import BeautifulSoup
from os import getcwd as cwd


avant = "https://jobs.lever.co/avant/1c9e827f-19da-49ea-91cd-cce64aea0b56"
offline_avant = "C:/Users/mthom/dvStuff/getajob/offline_html/Avant - Software Engineer.html"
target = "C:/Users/mthom/dvStuff/getajob/offline_output.txt"  # cwd() + "target.txt"


def get_page(url, online=True):
    # can get online or offline HTML files
    if online:
        html = requests.get(url).text
    else:
        html = open(url, 'r').read()
    return html



def main(sample_site):
    # TODO: If you can process this to remove all <script> and <style> tags,
    # TODO: Your return value will be easier to work with.

    page = get_page(sample_site, False)
    soup = BeautifulSoup(page, "html5lib").prettify()
    return soup


if __name__ == '__main__':
    s = main(offline_avant)
    with open(target, 'w', encoding='UTF-8') as file:
        for piece in s:
            file.write(str(piece))


