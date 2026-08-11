import requests
from bs4 import BeautifulSoup
import ytmusicapi

date = input("Enter the date to create a playlist with top100 songs during that time(YYYY-MM-DD):")
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

song_names = [song.get_text() for song in soup.find_all("h3",class_="chart-entry__title")]
artists = [artist.get_text() for artist in soup.find_all("span",class_="chart-entry__artist")]

print(song_names)
print(artists)