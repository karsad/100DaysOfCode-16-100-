import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
response.raise_for_status()
page_body = response.text

soup = BeautifulSoup(page_body, "html.parser")
titles = [movie.h2.strong.getText(strip=True) for movie in soup.find_all(name="span", class_="content_content__i0P3p") if movie.h2 and movie.h2.strong]

with open("100movies.txt", "a") as file:
    for title in titles[::-1]:
        file.write(title+"\n")