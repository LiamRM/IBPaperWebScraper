# IB-Paper-Web-Scraper
This program allows for users to easily generate links to IB papers from the IBDocuments website. These links are saved to a CSV file. No personal data is stored.

## Why I made it and how it works
In high school, I found myself spending a large amount of time sifting through the IBDocuments website to download test papers (for extra practice). This python script is intended to automatically generate a list of links to the PDFs of IB math papers via web scraping, WITHOUT having to click around the website. 
The user specifies the subject level (Higher Level or Standard Level), and the papers desired (P1, P2, P3), and links are obtained by scraping the IBDocuments.com website, which is then saved to a CSV file. This list of links can then be opened via the OpenList Google Chrome extension. 

## What I learned
- Web scraping using the Beautiful Soup module
- CSV file parsing

## :gear:Setup
1. First, make sure you have Python and Git installed on your computer. 
    * These are the Python download links for [Windows](https://www.python.org/downloads/windows/) and for [Mac](https://www.python.org/downloads/mac-osx/)
    * Git comes on most Macs and Linux machines, but if it is not installed, this [installation guide](https://github.com/git-guides/install-git#:~:text=To%20install%20Git%2C%20navigate%20to,installation%20by%20typing%3A%20git%20version%20.) may help.
2. Clone/download the git repo into a folder on your computer.
3. Open main.py and enter the respective search parameters (what subject, what IB papers desired)
4. In terminal, access the program folder and type "python3 main.py"
5. The program should run, displaying its progress collecting links for each year.
6. When the 'Done!' message appears, a CSV file titled 'cms_scrape.csv' should be created in the folder. Open it in Excel or another CSV reader and copy the links desired. 
7. Paste these links into OpenList, a free Google Chrome extension, and click 'Open' to open all the links.
    * If you do not have OpenList, it can be installed [here for free](https://chrome.google.com/webstore/detail/openlist/nkpjembldfckmdchbdiclhfedcngbgnl?hl=en).

Enjoy using this program and please feel free to contact me at lrm444@nyu.edu for any issues encountered!