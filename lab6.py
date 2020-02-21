import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


def add_to_table(array, posts):
    posts.insert_one(
        {"year": array[0], "country": array[1], "name": array[2], "subject": array[3], "specific": array[4]})


r = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО')
htmlC = r.text
soup = BeautifulSoup(htmlC, "html.parser")

i = 0
trs = soup.find_all('tr')

rowN = 6
results = []
for tr in trs:
    i += 1
    if str(tr).find("Направления научных исследований") > 0:
        break

for j in range(rowN):
    print(j)
    innerArr = []
    for td in BeautifulSoup(str(trs[j + i]), 'html.parser').find_all(['th', 'td']):
        innerArr.append(td.text.rstrip().replace(u'\xa0', u' '))
        print(td.text)

    results.append(innerArr)

print("--------132123-----------")
print(results)

# ---lab-specific code

client = MongoClient()
# client = MongoClient('localhost', 27017)
db = client.lab_6
posts = db.posts

for i in results:
    add_to_table(i, posts)
