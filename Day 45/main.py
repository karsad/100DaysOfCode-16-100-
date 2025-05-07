from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     page = file.read()
#
# soup = BeautifulSoup(page, "html.parser")
# print(soup.title)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

article_text = []
article_link = []

soup = BeautifulSoup(yc_web_page, "html.parser")
for span in soup.find_all(name="span", class_="titleline"):
    article_link.append(span.a.get('href'))
    article_text.append(span.a.getText())
article_upvote = [(score.getText()).split(" ")[0] for score in soup.find_all(name="span", class_="score")]

max_score = max(article_upvote)
idx = article_upvote.index(max_score)

print(f"Best article with: {article_upvote[idx]} score is: {article_text[idx]}\nLink: {article_link[idx]}")