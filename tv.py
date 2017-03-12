import urllib2
from bs4 import BeautifulSoup
quote_page = 'http://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv_4'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
list1=[]
for i in range(100):
 cont=soup.findAll('td', attrs={'class': 'titleColumn'})[i]
 fr=cont.text
 list1.append(fr)
for x in list1:
 print x;
