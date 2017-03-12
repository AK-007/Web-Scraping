import urllib2  
from bs4 import BeautifulSoup
quote_page = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('div', attrs={'class': 'lister'})
name = name_box.text
print name
