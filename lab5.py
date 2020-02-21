import pymysql
from pymysql.cursors import DictCursor
import requests
from bs4 import BeautifulSoup
import cryptography


def create_table(cursor):
    cursor.execute(
        'CREATE table IF NOT EXISTS lab5(year VARCHAR(10), country VARCHAR(40), name VARCHAR(40),' +
        'subject VARCHAR(100), specificity VARCHAR(100))')


def add_to_table(array, cursor):
    cursor.execute(
        'INSERT INTO lab5(year, country, name, subject, specificity) values ("' + array[0] + '", "' + array[1]
        + '","' + array[2] + '","' + array[3] + '","' + array[4] + '")')


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

connection = pymysql.connect(
    host='localhost',
    port=5432,
    user='root',
    password='Hydron063',
    db='db1',
    charset='utf8mb4',
    cursorclass=DictCursor
)

cur = connection.cursor()
create_table(cur)
for i in results:
    add_to_table(i, cur)
connection.commit()
connection.close()
