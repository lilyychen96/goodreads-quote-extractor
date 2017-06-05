# goodreads-quote-extractor

#### A script that fetches and downloads most popular quotes, optionally according to keyword.

This script will parse and download approx. 20 quotes from Goodreads based on keyword (e.g. word, author, tag, etc.), if provided. Lack of keyword outputs top ~20 quotes among Goodreads members.

## Installation:
This script is a Python (2.7) file and requires one installation with `pip install beautifulsoup4`

## Run:
Run the script with `python scrape.py` and input the desired keyword when prompted. Output file is "quotes.txt" but can be easily renamed by `mv quotes.txt desired_file_name.txt`
