import scraper
import filter

htmllist = scraper.pagedownload("https://www.goodwork.ca/volunteer/")
hreflist = scraper.linkscraper(htmllist)
finallist = scraper.infoscraper(hreflist)
filteredlist = filter.filterbylocation(finallist, "Toronto")

