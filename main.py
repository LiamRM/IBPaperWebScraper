import requests
from bs4 import BeautifulSoup

url = 'https://www.ibdocuments.com/IB%20PAST%20PAPERS%20-%20SUBJECT/Group%205%20-%20Mathematics/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

tablerow = soup.find('tr', class_='odd-dir')

#print(tablerow.prettify())

# Prints out the text grabbed from table
tabledatacell = tablerow.find('td', class_='indexcolname')
text = tabledatacell.a.text 
print(text)

#Other tutorial stuff

#with open('simple.html') as html_file:
#    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
#match = soup.find('div') #Finds the first div in the html file

# Loops through all the articles in the html file
#for article in soup.find('div', class_='article'):
    #print(article)

    #headline = article.h2.a.text 
    #print(headline)

    #summary = article.p.text 
    #print(summary)

    #print()