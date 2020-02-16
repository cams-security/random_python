from bs4 import BeautifulSoup
import re, csv
import feedparser
"""
Purpose is to grab iocs from https://paste.cryptolaemus.com/feed.xml and extract indicators and write it to a easily digestable format...
Under construction...
"""
ips = []
final_ips = []
urls = []
final_urls = []
url_whitelist = ["http://twitter.com", "https://twitter.com", "twitter.com", "https://capesandbox.com", "http://capesandbox.com", "capesandbox.com","https://avast.com", "http://avast.com", "avast.com", "https://cert.pl"]
def Grab_Feeds():
    return feedparser.parse("https://paste.cryptolaemus.com/feed.xml")

def Extract_Data():
    feed = Grab_Feeds()
    for entry in feed.entries:
        value = entry.content
        html = (value[0]['value']) #grabbing html from [0] [value] field.
        soup = BeautifulSoup(html) #cleaning it up with BeautifulSoup
        ip_values = re.findall('[0-9]+(?:\.[0-9]+){3}:[0-9]+', str(soup)) #Regex to catch [IP:Port] (ex: 127.0.0.1:80)
        url_values = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(soup)) #Regex to catch all URLs
        for ip in ip_values:
            ips.append(ip)
        for url in url_values:
            url = str(url).lower()
            if "http://twitter"


def Sort_Data():
    for ip in ips:
        ip = str(ip)
        ip_port = ip.split(":") #split to get IP and Port
        final_ips.append([ip_port[0], ip_port[1]])
      
    for x in final_ips:
        print("IP {0} at Port {1}".format(x[0],x[1]))

def Main():
    Extract_Data()
    Sort_Data()
    print("Complete. ")
Main()




##sha256 \b[a-zA-Z0-9]{64}\b
#md5 \b[a-zA-Z0-9]{32}\b
#sha1 \b[a-zA-Z0-9]{40}\b
