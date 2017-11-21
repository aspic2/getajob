# web scraper to help find good jobs

# TODO: Get list of training data (20 great jobs and 20 bad jobs).
# TODO: Scrape them and store word frequency in separate hash maps.

import requests
from bs4 import BeautifulSoup
from os import getcwd as cwd


avant = "https://jobs.lever.co/avant/1c9e827f-19da-49ea-91cd-cce64aea0b56"
target = "C:/Users/mthom/dvStuff/getajob/gab_output.txt"  # cwd() + "target.txt"

def main(sample_site):
    # TODO: If you can process this to remove all <script> and <style> tags,
    # TODO: Your return value will be easier to work with.
    r = requests.get(sample_site)
    soup = BeautifulSoup(r.text, "html5lib").prettify()
    words = soup
    return words


if __name__ == '__main__':
    s = main(avant)
    with open(target, 'w', encoding='UTF-8') as file:
        for piece in s:
            file.write(str(piece))


