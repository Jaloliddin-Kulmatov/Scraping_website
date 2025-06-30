from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
print(soup.title)

names_list = []
movies_names = soup.find_all(name="h3", class_="title")
for name in movies_names:
    names_list.append(name.text)
names_list.reverse()
print(names_list)

with open("movies.txt", "w") as file:
    for movie in names_list:
        file.write(f"{movie}\n")