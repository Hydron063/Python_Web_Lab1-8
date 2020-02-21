import requests
from bs4 import BeautifulSoup
import psycopg2


def add_to_table(array, cursor):
    cursor.execute(
        "INSERT INTO lab4_2 (year, country, name, subject, specificity) VALUES ('{" + array[0] + "}','{" + array[1] +
        "}','{" + array[2] + "}','{" + array[3] + "}','{" + array[4] + "}')"
    )


r = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО')
htmlC = r.text
soup = BeautifulSoup(htmlC, "html.parser")

i = 0
trs = soup.find_all('tr')

rowN = 6
results = []
for tr in trs:
    i += 1
    # print(tr)
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

conn = psycopg2.connect(dbname='db1', user='root', password='Hydron063', host="127.0.0.1", port="5432")
cur = conn.cursor()

for i in results:
    add_to_table(i, cur)

conn.commit()
conn.close()
