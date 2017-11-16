import requests
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from lxml import html

csvdata=[]

for x in range(2001,2017):
    pathurl='http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27214&timeframe=2&StartYear=1840&EndYear=2017&Day=31&Year=%d&Month=8#legendM' %(x)
    page = requests.get(pathurl)
    tree = html.fromstring(page.content)

    list=[]

    for i in range(2,29):
        url='//*[@id="dynamicDataTable"]/table/tbody/tr[%d]/td[4]/text()' %(i)
        data = tree.xpath(url)
        list.append(float(data[0]))

    csvdata.append(list)
    x=np.arange(0,27)
    spl = UnivariateSpline(x, list)
    spl.set_smoothing_factor(0.1)
    xs=np.linspace(0,26,1000)
    plt.plot(xs, spl(xs), 'b', lw=0.5)               # we can use the spl as a function
    print(list)

plt.show()
datafile=open('edmonton.csv','w')
with datafile:
    writer = csv.writer(datafile)
    writer.writerows(csvdata)
