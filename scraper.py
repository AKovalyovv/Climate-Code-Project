import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

def pagedownload(website, errorstring = "No exact matches found"): #Download a page for later usage
	html = ""
	htmllist = []
	i = "1"
	inum = 1
	while errorstring not in html:
		html = requests.get(website + i).text #Attempts to download the page
		htmllist.append(html)
		inum += 1
		i = str(inum)
	return htmllist

def linkscraper(htmllist, teststring = "/volunteer", originalwebsite = "https://www.goodwork.ca"): #Scrape the website for postings and return a list with the links to them
	hreflist = []
	for page in htmllist:
		soup = BeautifulSoup(page, 'html.parser')
		for a in soup.find_all('a'):
			if teststring in a.get('href'):
				hreflist.append(originalwebsite + a.get('href'))
	hreflist = list(set(hreflist))
	return hreflist

@dataclass
class VolunteerPosting:
	def __init__(self, name, details, organization, location, link):
		self.name = name  
		self.details = details
		self.organization = organization
		self.location = location  
		self.link = link

	name: str
	details: str
	organization: str 
	location: str
	link: str

def infoscraper(hreflist, checkstring = "Open/apply now."):
	jobinfo = []
	i = 0
	for link in hreflist:
		html = requests.get(link).text 
		if checkstring in html:
			soup = BeautifulSoup(html, 'html.parser')
			info = soup.title.text
			infolist = info.split(', ', 3)
			posting = VolunteerPosting("Name", "N/A", "Organization", "Location", "Link")
			jobinfo.append(posting)
			if (len(infolist) == 4):
				jobinfo[i].name = infolist[0]
				jobinfo[i].details = infolist[1]
				jobinfo[i].organization = infolist[2]
				jobinfo[i].location = infolist[3]
				jobinfo[i].link = link
				i += 1
			elif (len(infolist) == 1):
				del jobinfo[i]
			else:
				jobinfo[i].name == infolist[0]
				jobinfo[i].organization == infolist[1]
				jobinfo[i].location == infolist[2]
				jobinfo[i].link = link
				i += 1
			
			#jobinfo[i].contactinfo = [a["href"] for a in soup.select('a[href^=mailto:]')]
			
	return jobinfo