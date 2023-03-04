import scan_object
import host_object
import requests
from bs4 import BeautifulSoup

scanner = scan_object.scan_object()
#scanner.getSpamLevel("69.128.137.165")

host = host_object.host_object("69.128.137.165")
#host.readXML()

#host.readSpam()
#print(host.spamInfo)

host.readWhoIs()

