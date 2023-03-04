import subprocess
import whois
import requests
from bs4 import BeautifulSoup

class scan_object:

    def scanAddressRange(self, addressRange):
        # call subprocess here
        
        # don't need to return anything since this will just get saved to a file
        return

    def scanSingleAddress(self, singleAddress):
        # call subprocess here

        # don't need to return anything since this will just get saved to a file
        return 

    def getSpamLevel(self, singleAddress):
        #https://scamalytics.com/ip/69.128.137.165
        url = "https://scamalytics.com/ip/" + singleAddress
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        fraud_score_section = soup.find("div", class_="score") 
        score_text = fraud_score_section.get_text(strip=True)
        return score_text

    def getWhoIsData(self, singleAddress):
        data = whois.whois(singleAddress)
        return data.text
        # https://pypi.org/project/python-whois/

    def getPortData(self, portNum):
        return "https://www.speedguide.net/port.php?port=" + str(portNum)

    # port risk and links go in displaying code / different class?