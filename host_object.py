import xml.etree.ElementTree as ET
import scan_object


class host_object:
    # this will all stay public so don't worry about setters
    whoisInfo = ""
    portInfo = "| "
    spamInfo = ""
    address = ""

    scanner = scan_object.scan_object()

    def __init__(self, address, scanBoolean):
        self.address = address
        if scanBoolean == True:
            self.readSingleXML()
            self.readSpam()
            self.readWhoIs()
        return 

    # adds ports from nmap xml file to this object
    def readSingleXML(self):
        tree = ET.parse('singles/' + self.address + '.xml')
        root = tree.getroot()
        for port in root.findall('.//port'):
            port_id = port.get('portid')
            self.portInfo = self.portInfo + str(port_id) + " | "

    # adds the spam level to this object
    def readSpam(self):
        self.spamInfo = self.scanner.getSpamLevel(self.address)

    def readWhoIs(self):
        self.whoisInfo = self.scanner.getWhoIsData(self.address)

    def __str__(self):
        return "ADDR: " + self.address + "\n" + "PORTS: " + self.portInfo + "\n" + "FRAUD LEVEL: " + self.spamInfo + "\n" + self.whoisInfo + "\n"


    

