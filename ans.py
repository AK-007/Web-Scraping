import urllib2
from bs4 import BeautifulSoup
quote_page = 'http://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv_4'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
list1=[]
v={}
for i in range(100):
 cont=soup.findAll('td', attrs={'class': 'titleColumn'})[i]
 fr=cont.text
 list1.append(fr)
for k in list1:
  v[k]=1
h=list1[0]
g=0
for link in soup.select('td.titleColumn a[href]'):
     v[h]=link
     g=g+1
     if g==100 :break
     h=list1[g]
     
for key,val in v.items():
    print key, "=>", val


 
