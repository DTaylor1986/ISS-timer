#print out the next time the space station flies over
# data read from https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=Wales&city=Swansea#.Y4OtJzPP1uQ

import feedparser
from datetime import datetime

def clean_data(summary):
    details = summary.split('<br />')
    for x in range(len(details)):
       details[x] = details[x].strip()
       if x == 0:
            # convert the string text to datetime
            # example: 'Date: Monday Nov 28, 2022'
            details[0] = datetime.strptime(details[0], 'Date: %A %b %d, %Y')
    return details

#retreive xml from website
xml_doc = feedparser.parse("https://spotthestation.nasa.gov/sightings/xml_files/United_Kingdom_Wales_Swansea.xml")


#work through the list of ISS passovers
passovers = []
for i in range(len(xml_doc)):
    entry = xml_doc.entries[i] 
    summary = str(entry['summary'])
    passover = clean_data(summary)
    passovers.append(passover)

#check to see if the latest works
print(passovers[0][0])