import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies_raw = soup.select(name="h3",selector=".title")

movies_list_reversed = []
for movie in movies_raw:
    movies_list_reversed.append(movie.get_text())


movies_list = movies_list_reversed[::-1]

with open("Top100Movies.txt","w") as file:
    for num in range(100):
        try:
            file.write(f"{movies_list[num]}\n")
        except UnicodeEncodeError:
            words = movies_list[num].split()
            valid_words = []
            for word in words:
                try:
                    word.encode("ascii")
                    valid_words.append(word)
                except UnicodeEncodeError:
                    continue
            full_word = " ".join(valid_words)
            file.write(f"{full_word}\n")

