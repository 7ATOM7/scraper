#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
import pandas as pd
import time


# In[15]:

print('Importing Done')
url = 'http://books.toscrape.com/'
user_agent = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 RuxitSynthetic/1.0 v2133633816 t7283065708159130298 smf=0'}
req = requests.get(url,user_agent)
time.sleep(1)
print('Got first URL')
soup_books_list = BeautifulSoup(req.text,features="html.parser").find('section').find('ol').find_all('li')


# In[17]:


k=1
final_result=[]
while k <= 50:
    url_page='http://books.toscrape.com/catalogue/page-'+str(k)+'.html'
    req = requests.get(url_page,headers=user_agent)
    time.sleep(1)
    print(k,url_page)
    soup_books_list = BeautifulSoup(req.text,features="html.parser").find('section').find('ol').find_all('li')
    j=0
    for i in soup_books_list:
        new_url = url +'catalogue/' + soup_books_list[j].find('a').attrs['href']
        req2 = requests.get(new_url,headers=user_agent)
        time.sleep(1)
        soup = BeautifulSoup(req2.text,features="html.parser")
        a=[soup.find_all('h1')[0].string,soup.find_all('p',{'class':'price_color'})[0].string,soup.find_all('p',{'class':'instock availability'})[0].text.strip(' \n\t'),soup.find_all('p',{'class':'star-rating'})[0].attrs['class'][1],soup.find_all('ul')[0].find_all('a')[2].string,'http://books.toscrape.com/' + soup_books_list[0].find('a').find('img').attrs['src']]
        final_result.append(a)
        j=j+1
        print('inside page' + str(k) + 'book number' + str(j))

    k=k+1


# In[18]:


#for i in range(1,50):
#    print(requests.get('http://books.toscrape.com/catalogue/page-'+ chr(i) + '.html')


# In[21]:


df_books  =pd.DataFrame(final_result)
df_books.columns=['Name','Price','Availability','Rating','Section','Image_Link']


# In[26]:


req = requests.get(url,headers = user_agent)
time.sleep(.5)


# In[28]:


section_list=[]
for i in BeautifulSoup(req.text,features="html.parser").find('aside').find_all('li'):
    section_list.append([i.find('a').string.strip(' \n\t'),'http://books.toscrape.com/'+i.find('a').attrs['href']])


# In[31]:


df_sections = pd.DataFrame(section_list)
df_sections.columns = ['Section','Link']


# In[34]:


df_sections.to_csv('sections')
df_sections.to_csv('Books')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
df_books.to_sql('books_pandas', engine)
df_sections.to_sql('sections_pandas',engine)

