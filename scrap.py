import requests
import csv
from lxml import html

csvdata=[]

for x in range(2001,2016):
    pathurl='http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27214&timeframe=2&StartYear=1840&EndYear=2017&Day=31&Year=%d&Month=1#legendM' %(x)
    page = requests.get(pathurl)
    tree = html.fromstring(page.content)
    list=[]
    print(x)
    for i in range(2,33):
        url='//*[@id="dynamicDataTable"]/table/tbody/tr[%d]/td[4]/text()' %(i)
        data = tree.xpath(url)
        list.append(float(data[0]))
    csvdata.append(list)
    print(list)

datafile=open('edmonton.csv','w')
with datafile:
    writer = csv.writer(datafile)
    writer.writerows(csvdata)
