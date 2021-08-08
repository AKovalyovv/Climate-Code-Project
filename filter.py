from scraper import VolunteerPosting

def filterbylocation(datalist, location):
	filteredlist = []
	for posting in datalist:
		if location.lower() in posting.location.lower():
			filteredlist.append(posting)
	return filteredlist
