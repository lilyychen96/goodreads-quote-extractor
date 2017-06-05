# Scraping quotes from Goodreads
# Based on keywords
# (e.g. actual keywords, tags, authors)

import sys
import requests
import string
from bs4 import BeautifulSoup


def make_printable(corpus):
  new_corp = filter(lambda x: x in string.printable, corpus)
  return new_corp


def write_file(path, corpus):
  with open(path, "w") as f:
    f.write(corpus)
    f.close()


def scrape(keyword=""):
  # Default is "Quotes popular among Goodreads members"
  url = "http://www.goodreads.com/quotes"

  if (keyword != ""):
    url = "http://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q="+keyword

  request = requests.get(url)
  soup = BeautifulSoup(request.content, "html.parser")

  # Convert <br/> elements to new lines
  # Allows for multi-line quotes and poems
  for br in soup.find_all("br"):
    br.replace_with("\n")

  # Extract only from quoteText class
  quote_txt = soup.find_all("div", attrs={"class":"quoteText"})

  corpus = ""

  for q in quote_txt:
    author = ""

    # If unable to retrieve author, then something probably messed up
    # So... just skip over it
    try:
      author = q.find("a").get_text() + "\n"
    except:
      continue

    quote = ""

    # Concatenate multi-line quotes/poems into a single string
    for i in xrange(len(q.contents)):
      line = q.contents[i].encode("ascii", errors="ignore").decode("utf-8")
      if (line[0] == "<"): # is a tag
        break
      else:
        quote += line

    q.contents[0] = quote

    quote = q.contents[0].encode("ascii", errors="ignore").decode("utf-8")
    quote = "\"" + quote.strip() + "\" "

    corpus += quote + "\n" + author + "\n"

  return corpus


def main():
  prompt = "Enter keyword, author, etc. (press enter to see popular quotes): "
  keyword = raw_input(prompt)
  if (keyword != ""):
    print("Looking for quotes relating to ~%s~..." % keyword)
  else:
    print("Looking through Goodread's most popular quotes...")

  print("Scraping from Goodreads...")
  quotes = make_printable(scrape(keyword))

  print("Writing contents to local file...")
  write_file("quotes.txt", quotes)

  print("Done! Please check out quotes.txt")


if __name__ == '__main__':
  main()
