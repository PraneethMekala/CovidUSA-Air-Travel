#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:39:08 2020

@author: praneeth mekala
"""

"""Part C for Project 6Updated on 11/18/2020by William Yu"""
import requestsimport urllib.requestfrom bs4 
import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os
#######################
# TSA travel data#
######################
# Reading the web page into Python
os.chdir("~/Desktop/Data Science bootcamp/Week 6/Project 06")

url = 'https://www.tsa.gov/coronavirus/passenger-throughput'
response = requests.get(url)
html = requests.get(url).content
soup = BeautifulSoup(response.text)
tsa1 = soup.find('table')
df1 = pd.read_html(str(tsa1))[0]


url = 'https://www.tsa.gov/coronavirus/passenger-throughput?page=1'
response = requests.get(url)
html = requests.get(url).content
soup = BeautifulSoup(response.text)
tsa2 = soup.find('table')
df2 = pd.read_html(str(tsa2))[0] 

df3= pd.concat([df1, df2], axis=0)

df3.columns=['date','travel2020','travel2019']
df3.info()
df3['date'] = pd.to_datetime(df3['date']) 
df3['travel2020'] = pd.to_numeric(df3['travel2020'])/1000000
df3['travel2019'] = pd.to_numeric(df3['travel2019'])/1000000
df3.info()

df4 = df3.set_index('date')
df4.info()
df4.plot()

# Alternative Way
plt.figure(figsize=(12,8))
df4.travel2020.plot(grid=True, label="Air Travel 2020", marker='o',markersize=6, color='r')
df4.travel2019.plot(grid=True, label="Air Travel 2019", markersize=8, color='b')
plt.title("US Daily Travelers Through TSA Checkpoints",fontsize=15)
plt.ylabel('# Travelers (Million People)')
plt.xticks(fontsize=9)
plt.legend(loc="right",borderaxespad=3)
plt.savefig('TSA.png')
# plt.show()