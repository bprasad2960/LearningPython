#Author: Littl
# CreatedDate: 9th July 2021 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  print(type(theJSON))  #dictionary 
  #for i in theJSON["metadata"]["url"]:
      #print(i)
      #print(theJSON["metadata"][i])
  print(theJSON["metadata"])
  # output the number of events, plus the magnitude and each event name  
  #for i in theJSON["features"]:
       # print(theJSON["metadata"]["generated"],"\t" ,theJSON["metadata"]["url"],
       # "\t",theJSON["metadata"]["title"])
  print("Events count is :" , str(theJSON["metadata"]["count"]))
  
  for each in theJSON["features"]:
    print(each["properties"]["mag"], "\t", each["properties"]["title"])
       
  
  # for each event, print the place where it occurred
  for each in theJSON["features"]:
    print(each["properties"]["mag"], "\t", each["properties"]["place"])

  # print the events that only have a magnitude greater than 4
  for each in theJSON["features"]:
    if(each["properties"]["mag"]>4.0):
        print(each["properties"]["mag"], "\t", each["properties"]["place"],"\t", each["properties"]["felt"])

  # print only the events where at least 1 person reported feeling something
  for each in theJSON["features"]:
    if(each["properties"]["felt"] != None):
        print(each["properties"]["mag"], "\t", each["properties"]["place"],"\t", each["properties"]["felt"])

  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if(webUrl.getcode() ==200):
      printResults(webUrl.read())
  else:
      print("Unable to retrieve the web page!")  

if __name__ == "__main__":
  main()
