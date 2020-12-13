import requests
from bs4 import BeautifulSoup
import csv

# Setting up the search variables
startYear = '2000'
endYear = '2019'
paper1 = True
paper2 = True
paper3 = True
withMarkscheme = True       #please type 'True' or 'False'
hl = True                   #if HL = 'False', then SL papers will be downloaded

# Don't change these
url = 'https://www.ibdocuments.com/IB%20PAST%20PAPERS%20-%20SUBJECT/Group%205%20-%20Mathematics/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
urlList = []
availableYears = []
examSessionLinks = []
availablePapers = []
paperLinks = []

# Compiling list of subject links
for tabledata in soup.find_all('td', class_='indexcolname'):
    urlList.append(tabledata.a.text) 

print("Url List:", urlList)
print()
# Creating links to the subjects (methods, studies, further, etc...)
subjUrl = f'{url}{urlList[3]}'      
print(subjUrl)
subjSoup = BeautifulSoup(requests.get(subjUrl).text, 'lxml')

print()
for tabledata in subjSoup.find_all('td', class_='indexcolname'):
    availableYears.append(tabledata.a.text)
print(availableYears)

# Looping through years to check for matching starting year
for year in availableYears:
    print(year[:4])
    if year[:4] == startYear:               #gets the first 4 characters of string, inclusive
        print('Matching year! ', startYear)
        validStartYear = True
        # need a way to get the index

# If match, generate new links
if validStartYear == True:
    for year in availableYears:
        examSessionUrl = f'{subjUrl}{year}'
        examSessionLinks.append(examSessionUrl)

print(examSessionUrl)
# Using latest examSessionUrl as a test
examSessionSoup = BeautifulSoup(requests.get(examSessionUrl).text, 'lxml')
for tabledata in examSessionSoup.find_all('td', class_='indexcolname'):
    availablePapers.append(tabledata.a.text)
print(availablePapers)

# Taking relevant papers from available into paperLinks Lists
for paper in availablePapers:
    if paper.__contains__('French'):
        pass
    elif paper.__contains__('Spanish'):
        pass
    else:
        # Create link to paper
        paperUrl = f'{examSessionUrl}{paper}'
        paperLinks.append(paperUrl)
print(paperLinks)

# CSV Setup
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Paper title', 'year', 'PDF Link']) #Writing a list of values

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