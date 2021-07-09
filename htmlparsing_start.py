# Author: Littl
# CreatedDate: 9th July 2021 
# Example file for parsing and processing HTML
#

from html.parser import HTMLParser

metaCount = 0 

class myHTMLParser(HTMLParser):

  def handle_starttag(self, tag,attrs):
      global metaCount
      pos = self.getpos()
      #print("Encountered a tag ",tag," in line ", pos[0]," at position ",pos[1])
      #print(pos)
      #print(type(pos)) #method
      #print(tag ,"\t", attrs)
   #count the number of meta tags
      if (tag == "meta"):
        metaCount += 1
        print(metaCount)
         
  def handle_data(self, data):
      print(data)



def main():
  # instantiate the parser and feed it some HTML
  parser = myHTMLParser()

  f = open("samplehtml.html",'r')
  contents = f.read()
  parser.feed(contents)
  print("Total meta tag count is: ", metaCount)

if __name__ == "__main__":
  main();
  