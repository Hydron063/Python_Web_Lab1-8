import requests
import pandas as pd
import csv

html = requests.get('https://ru.wikipedia.org/wiki/Университет_ИТМО').content
df_list = pd.read_html(html)

for i, df in enumerate(df_list):
    # print(df)
    if i == 3:
        df.to_csv('table {}.csv'.format(i))

results = []
with open("table 3.csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)  # change contents to strings
    for row in reader:  # each row is a list
        results.append(row)

print(results)

f = open("lab1res.txt", "w+")
for ind in range(len(results) - 1):
    i = results[ind + 1]
    f.write('В году ' + i[1] + ' в стране с названием ' + i[2] + ' человек по имени ' +
            i[3] + ' создал научно подразделение в области ' + i[4] + ', а именно по направлению ' + i[5] + '\n\n')
