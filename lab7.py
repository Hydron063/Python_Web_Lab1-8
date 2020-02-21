import os
import sqlite3
import requests
from bs4 import BeautifulSoup
from http.server import HTTPServer, CGIHTTPRequestHandler


def add_to_table(array, cursor):
    cursor.execute(
        'INSERT INTO lab7 (year, country, name, subject, specific) values ("' + array[0] + '", "' + array[1] + '","' +
        array[2] + '","' + array[3] + '","' + array[4] + '")')


r = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО')
htmlC = r.text
soup = BeautifulSoup(htmlC, "html.parser")

i = 0
trs = soup.find_all('tr')

rowN = 6
results = []
for tr in trs:
    i = i + 1
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

conn = sqlite3.connect('./lab7.sqlite')
cur = conn.cursor()

cur.execute(
    'CREATE TABLE IF NOT EXISTS lab7 (year VARCHAR, country VARCHAR, name VARCHAR, subject VARCHAR, specific VARCHAR)')

for i in results:
    add_to_table(i, cur)
conn.commit()
conn.close()

# The connection to DB part

count = 0
directory = "./cgi-bin/"
if not os.path.exists(directory):
    os.makedirs(directory)

for i in results:
    string = '''#!/usr/bin/env python3

print("Content-type: text/html")
print()
print("<h1>В году {} в стране {} человек по имени {} преуспел в области {} по спецификации {}</h1>")'''.format(*i)

    f = open(directory + str(count) + ".py", "w", encoding='utf-8')
    f.write(string)
    count = count + 1

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
