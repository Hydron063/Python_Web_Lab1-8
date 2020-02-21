import sqlite3
import requests
from bs4 import BeautifulSoup


def add_to_table(array, cursor):
    cursor.execute(
        'INSERT INTO lab3 (year, country, name, subject, specific) values ("' + array[0] + '", "' + array[
            1] + '","' +
        array[2] + '","' + array[3] + '","' + array[4] + '")')


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

conn = sqlite3.connect('lab3.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS lab3 (year, country, name, subject, specific)')

for i in results:
    add_to_table(i, cur)
conn.commit()
conn.close()

conn = sqlite3.connect('lab3.sqlite')
cur = conn.cursor()
cur.execute('SELECT * FROM lab3')
print('-------Verification--------\n', cur.fetchall())
