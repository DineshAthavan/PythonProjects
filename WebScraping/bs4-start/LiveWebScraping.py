from bs4 import BeautifulSoup
import requests


response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

Text = soup.select(name="a",selector="span.titleline")

info = []
links = []
num_votes = []
for article in Text:
    info.append(article.get_text())

for article in Text:
    link_text = article.find('a')
    links.append(link_text.get("href"))

upvotes = soup.select(name="span",selector=".score")
for upvote in upvotes:
    num_votes.append(int(upvote.get_text().split()[0]))

print(info)
print(links)
print(num_votes)

max_votes_location = num_votes.index(max(num_votes))
print("Popular article:")
print(f"Title: {info[max_votes_location]}")
print(f"Link: {links[max_votes_location]}")
print(f"Number of votes: {num_votes[max_votes_location]}")