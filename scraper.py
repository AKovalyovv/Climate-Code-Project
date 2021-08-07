import requests
from bs4 import BeautifulSoup

def pagedownload(website): #Download a page for later usage
	html = ""
	htmllist = []
	i = "1"
	inum = 1
	while "No exact matches found" not in html:
		page = requests.get(website + i) #Attempts to download the page
		html = page.text
		htmllist.append(html)
		inum += 1
		i = str(inum)
	return (htmllist)

def linkscraper(htmllist, teststring = "/volunteer", originalwebsite = "https://www.goodwork.ca"): #Scrape the website for postings and return a list with the links to them
	hreflist = []
	for page in htmllist:
		soup = BeautifulSoup(page, 'html.parser')
		for a in soup.find_all('a'):
			if teststring in a.get('href'):
				hreflist.append(originalwebsite + a.get('href'))
	hreflist = list(set(hreflist))
	return hreflist
	



    
