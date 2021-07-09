#Author:Littl
# CreatedDate: 9th July 2021 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
    webUrl = urllib.request.urlopen("https://www.google.com")
    print("WebURL output is:" + str(webUrl.getcode()))
    print(type(webUrl.getcode()))
    print(webUrl.read())
    print(type(webUrl.read()))
    
    

if __name__ == "__main__":
  main()
