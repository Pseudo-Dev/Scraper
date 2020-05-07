import scrapy
import re

class ChristSpider(scrapy.Spider):
    name = 'christ_spider'
    url = input("Paste the URL here: ") #Get the URL input
    start_urls = [url] 
    
    def parse(self, response):
        for siteData in response.xpath("/html//div[@class='col-md-9 col-sm-9 alignment']//p").extract(): #Extract only the middle section of the webpage
            cleanText = tagRemover (siteData) #Remove all HTML Tags from the webpage
            if cleanText.find("PO") != -1 or cleanText.find("PSO") != -1 or cleanText.find("On completion") != -1: #Search for PO, PSO or similar keywords
                for writeData in cleanText: #If found, wrte it into the csv file
                    csvCreator(writeData)

        for siteData in response.xpath("/html//div[@class='col-md-9 col-sm-9 alignment']//ul").extract(): #Does the same as above, but some are written as lists so this is for those
            cleanText = tagRemover (siteData)
            if cleanText.find("PO") != -1 or cleanText.find("PSO") != -1 or cleanText.find("On completion") != -1:
                csvCreator(cleanText)


def tagRemover (siteData): #This function removes all the HTML tags from the extracted webpage
    clean = re.compile('<.*?>')
    return(re.sub(clean, '', siteData))

def csvCreator(data): #This function creates the CSV. Please note, its in append mode. Accordingly change as you wish
    csvFile = open("scrapedData.csv", "a")
    csvFile.write(data)
    csvFile.close()