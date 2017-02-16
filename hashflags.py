# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from lxml import html
import requests
# download twitter html
page = requests.get('http://twitter.com')
tree = html.fromstring(page.content)
# select #init-data value property
x = tree.xpath('//*[@id="init-data"]/@value')
import json
# parse json from #init-data
parsed_json = json.loads(x[0])
xk = parsed_json['activeHashflags']
import csv
import time
# save file in current directory
# example fn hashflags021617.csv
timestr = time.strftime("%m%d%y")
hashflag_data = open('hashflags' + timestr + '.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(hashflag_data, delimiter=',')
csvwriter.writerow(['hashflag','location'])
for i in xk:
        print(i + ',' + xk[i])
        csvwriter.writerow([i,xk[i]])
hashflag_data.close()
