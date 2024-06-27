import requests
from bs4 import BeautifulSoup
import mysql.connector
url = "https://www.prothomalo.com/sports/cricket/nuvv7vrfgm"

#C201091, Get HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#C201091, Parse HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)

#C201091, HTML Tree Travelsar
title = soup.title
#print(type(title))
#print(type(soup))
#print(type(title.string))

para = soup.find_all('p')
#print(para)
anchor = soup.find_all('a')
#print(anchor)
datas = soup.find_all("li")
#print(soup.find('p')['class'])
#print(soup.find('p').get_text)
all_links = set()
for link in anchor:
    if(link.get('href') != '#'):
        linkText = "https://www.prothomalo.com/sports/cricket/nuvv7vrfgm"+link.get('href')
        all_links.add(link)
        #print(linkText)



category_id = soup.find(id = "header")
title = soup.find('h1')[1].text
reporter_id = soup.find(id = "author")
publisher_id = soup.find(id = "publisher")
datetime = soup.find('td', class_='date').get_text().strip()
body = soup.find('p')
link = soup.find('url')

 #C201091,DB Connector
db = mysql.connector.connect(user='root', password='97727247',
                              host='8.20.27',
                              database='webscrapping')
cursor = db.cursor()
add_news = ("INSERT INTO sport"
                "(category_id, reporter_id, publisher_id, datetime, title, body, link)"
                "VALUES (%s, %s, %s, %s, %s)")
data_news = (category_id, reporter_id, publisher_id, datetime, title, body, link)

 #insertion
cursor.execute(add_news)

db.commit()
cursor.close()
db.close()