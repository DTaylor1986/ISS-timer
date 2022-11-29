#print out the next time the space station flies over
# data read from https://spotthestation.nasa.gov/sightings/view.cfm?country=United_Kingdom&region=Wales&city=Swansea#.Y4OtJzPP1uQ

import feedparser
import datetime

#retreive xml from website
xml_doc = feedparser.parse("https://spotthestation.nasa.gov/sightings/xml_files/United_Kingdom_Wales_Swansea.xml")


#work through the list of ISS passovers
for i in range(len(xml_doc)):
    entry = xml_doc.entries[i] 
    summary = str(entry['summary'])
    details = summary.split('<br />')
    #going to need to extract the date using strftime method from datetime

    for detail in details:
       print(detail.strip())