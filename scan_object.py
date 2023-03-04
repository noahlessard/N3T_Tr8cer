import subprocess
import whois
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class scan_object:

    iplist = []


    def scanAddressRange(self, addressRange):

        # example command
        # nmap -sP -oX singles/test.xml -F 69.128.137.0/24

        cmd_str = "nmap -sP -oX singles/" + str(addressRange[:-3]) + ".xml " + str(addressRange) 
        #subprocess.run(cmd_str, shell=True)

        tree = ET.parse('singles/' + str(addressRange[:-3]) + '.xml')
        root = tree.getroot()
        for address in root.findall('.//address'):
            self.iplist.append(str(address.get('addr')))

        return

    def scanSingleAddress(self, singleAddress):

        # example command 
        # nmap -oX singles/test.xml -F 69.128.137.165

        cmd_str = "nmap -oX singles/" + str(singleAddress) + ".xml -F " + str(singleAddress) 
        subprocess.run(cmd_str, shell=True)

        return 

    # run to clean up the singles dir
    def cleanupSingles(self):
        cmd_str = "rm -f singles/*"
        subprocess.run(cmd_str, shell=True)

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
        formattedString = "NAME: " + str(data.name) + "\n" + "ORG: " + str(data.org) + "\n" + "LOCATION: " + str(data.address) + " " + str(data.city) + " " + str(data.state) + " " + str(data.country) + "\n" + "DOMAIN: " + str(data.domain_name[0]) + "\n" + "LAST UPDATE: " + str(data.updated_date[0]) + "\n" + "EXP DATE: " + str(data.expiration_date) + "\n" + "EMAILS: " + str(data.emails[0]) + "\n" + "DNS STATUS: " + str(data.dnssec) 
        return formattedString
        # https://pypi.org/project/python-whois/

    def getPortData(self, portNum):
        return "https://www.speedguide.net/port.php?port=" + str(portNum)

    # port risk and links go in displaying code / different class?