import scan_object
import host_object
import requests
from bs4 import BeautifulSoup

scanner = scan_object.scan_object()

#scanner.scanSingleAddress("69.128.137.165")
#scanner.cleanupSingles()

scanner.scanAddressRange("69.128.137.0/24")

hostList = []

index = 0
while index < 4:
    scanner.scanSingleAddress(scanner.iplist[index])
    hostList.append(host_object.host_object(scanner.iplist[index]))
    index = index + 1

print("\n\n\n\n")

for x in hostList:
    print(x)

#host = host_object.host_object("69.128.137.165")
#host.readXML()

#host.readSpam()
#print(host.spamInfo)

#host.readWhoIs()

