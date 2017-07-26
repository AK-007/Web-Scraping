import urllib2
import pickle
from bs4 import BeautifulSoup
quote_page = 'http://www.imdb.com/chart/tvmeter?ref_=nv_tvv_mptv_4'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
list1=[]
v={}
bi={}
for i in range(50):
 cont=soup.findAll('td', attrs={'class': 'titleColumn'})[i]
 fr=cont.text
 list1.append(fr)
 bi[fr]=[]
for k in list1:
  v[k]=1
h=list1[0]
list2=[]
g=0
b='http://imdb.com'
c='keywords'
for link in soup.select('td.titleColumn a[href]'):
     x=str(link)
     w=x.split(' ')[1].strip("href=").strip('"')
     w=b+w
     s=w.split('?')[0]
     s=s+c
     v[h]=s
     pages=s
     da=urllib2.urlopen(pages)
     soup=BeautifulSoup(da,'html.parser')
     for links in soup.select('div.sodatext a[href]'):
       frw=links.text
       bi[h].append(frw)
     g=g+1
     if g==50 :break
     h=list1[g]
pickle.dump(bi,open("aaa.txt","wb"))
for key,val in bi.items():
    print key, "=>", val

 
