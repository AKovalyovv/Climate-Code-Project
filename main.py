import scraper

htmllist = scraper.pagedownload("https://www.goodwork.ca/volunteer/")
hreflist = scraper.linkscraper(htmllist)
finallist = scraper.infoscraper(hreflist)
