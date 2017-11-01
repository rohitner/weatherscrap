import requests
from lxml import html

for x in range(2001,2017):
    pathurl='http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27214&timeframe=2&StartYear=1840&EndYear=2017&Day=31&Year=%d&Month=8#legendM' %(x)
    page = requests.get(pathurl)
    tree = html.fromstring(page.content)

    list=[]
    list.append(x)

    for i in range(2,29):
        url='//*[@id="dynamicDataTable"]/table/tbody/tr[%d]/td[4]/text()' %(i)
        data = tree.xpath(url)
        list.append(float(data[0]))

    print(list)
