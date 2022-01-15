from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

score_list = []
rows = soup.find_all(name="td", class_="subtext")
for row in rows:
    score = row.find(name="span", class_="score")
    if score is None:
        score_list.append("0 points")
    else:
        score_list.append(score.getText())

article_upvotes = [int(score.split()[0]) for score in score_list]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(f"{article_upvotes[largest_index]} points")



# with open("website.html", encoding="UTF8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# # headings = soup.select("a")
# # print(headings)
#
# all_tags = soup.find_all(name="a")
# print(all_tags)
#
# for tag in all_tags:
#     print(tag.get("href"))

