# Ideas for tool #

1. Search job boards (or specific company pages) for job postings with certain
keywords.  
2. Create rules for #1 using training data of jobs that I like 
and jobs that I don't like. 


## What do you want to accomplish with this tool? ##

1. Answer "What skills do I need for my dream job?"
    - definitive list to add direction to my future projects
    
2. Notification when _perfect_ jobs appear at my favorite companies and boards.

3. Better keyword searches for jobs when using traditional boards

4. Find the best title to describe what I want to do.

## How do you propose accomplishing these things? ##

- Training data
    - Scrape some appealing job postings and create a hash table of every word that occurs.
    Filter out useless words (e.g. "the", "and"), and sort words by frequency.
 
    - Do the same for some unappealing jobs. 
 
    - Write a scraper to scan websites like remoteok.io and find jobs with many
    appealing words and few unappealing words
    
## ISSUES THUS FAR ##
Trouble parsing different webpages:
    - <style> and <script> elements making it through filters
    - punctuation interfering with word frequency count
    - plural words counted separately
    
