import urllib2
from bs4 import BeautifulSoup
import csv

quote_page = 'http://caldining.berkeley.edu/menu.php'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h3', attrs={'location2'})

name = name_box.text.strip()

table = soup.find_all('div', attrs={"class" : "menu_wrap_overall"})
lst = []
for div in table:
    for item in div.find_all(['p', 'h3']):
    	lst.append(item.text.strip())

with open('index.csv', 'w') as csv_file:
	writer=csv.writer(csv_file)
	for t in lst:
	    writer.writerow([t])