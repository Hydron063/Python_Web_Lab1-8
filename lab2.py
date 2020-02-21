import requests
from bs4 import BeautifulSoup

html = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО')
htmlC = html.text
soup = BeautifulSoup(htmlC, "html.parser")

# Находим строки таблицы
trs = soup.find_all('tr')

# Находим номер строки с нужной частью таблицы
i = 0
for tr in trs:
    i += 1
    # print(tr)
    if str(tr).find("Направления научных исследований") > 0:
        break

# Кол-во строк в таблице
rowN = 6
results = []
for j in range(rowN):
    print(j)
    innerArr = []
    # Находим строки с ячейками
    for td in BeautifulSoup(str(trs[j + i]), 'html.parser').find_all(['th', 'td']):
        innerArr.append(td.text.rstrip().replace(u'\xa0', u' '))
        print(td.text)

    results.append(innerArr)

print("--------132123-----------")
print(results)

emptyN = 0
f = open("lab2res.txt", "w+")
for ind in range(len(results) - 1):
    i = results[ind + 1]
    f.write('В году ' + i[emptyN + 0] + ' в стране с названием ' + i[emptyN + 1] + ' человек по имени ' + i[emptyN + 2]
            + ' сделал научно подразделение в области ' + i[emptyN + 3] + ' конкретно - в сфере ' + i[emptyN + 4]
            + '\n\n')
