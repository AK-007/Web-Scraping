import urllib2  
from bs4 import BeautifulSoup
quote_page = 'http://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv_4'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
list1=['']
title_box = soup.find('td', attrs={'class': 'titleColumn'})
title= title_box.text
list1.append(title)
print list1[1]
