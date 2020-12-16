import requests
from bs4 import BeautifulSoup
import csv

# Setting up the search variables
paper1 = True
paper2 = True
paper3 = True
tz0 = True
tz1 = True
tz2 = True
withMarkscheme = True       #please type 'True' or 'False'
hl = True                   #if HL = 'False', then SL papers will be downloaded

# Don't change these
url = 'https://www.ibdocuments.com/IB%20PAST%20PAPERS%20-%20SUBJECT/Group%205%20-%20Mathematics/'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
urlList = []
availableYears = []
availablePapers = []
availablePaperYears = []            # associating a year with each available paper
examSessionLinks = []               # associating an exam session URL with each available paper

# CSV Setup
csv_file = open('cms_scrape.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Paper title', 'year', 'PDF Link']) #Writing a list of values

# Compiling list of subject links
for td in soup.find_all('td', class_='indexcolname'):
    urlList.append(td.a.text) 

print("Url List:", urlList)
print()
# Creating links to the subjects (methods, studies, further, etc...)
subjUrl = f'{url}{urlList[4]}'      
print(subjUrl)
subjSoup = BeautifulSoup(requests.get(subjUrl).text, 'lxml')

print()
for td in subjSoup.find_all('td', class_='indexcolname'):
    availableYears.append(td.a.text)
print(availableYears)

# Generate new links to yearly exam session
for year in availableYears:
    examSessionUrl = f'{subjUrl}{year}'

    # Using latest examSessionUrl as a test
    examSessionSoup = BeautifulSoup(requests.get(examSessionUrl).text, 'lxml')
    for td in examSessionSoup.find_all('td', class_='indexcolname'):
        availablePapers.append(td.a.text)
        availablePaperYears.append(year)
        examSessionLinks.append(examSessionUrl)

    print("Generating links for ", year, "...")

# Taking relevant papers from available into paperLinks Lists
for i, paper in enumerate(availablePapers):
    if paper.__contains__('French') or paper.__contains__('Spanish') or paper.__contains__('Parent'):
        pass
    else:
        # Create link to paper (getting English papers only)
        currentYear = availablePaperYears[i]
        examSessionUrl = examSessionLinks[i]
        paperUrl = f'{examSessionUrl}{paper}'
        csv_writer.writerow([paper, currentYear, paperUrl])             # writing row to csv

print("Done!")
csv_file.close()

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