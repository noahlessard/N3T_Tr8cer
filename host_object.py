import xml.etree.ElementTree as ET
import scan_object


class host_object:
    # this will all stay public so don't worry about setters
    whoisInfo = ""
    portInfo = "| "
    spamInfo = ""
    address = ""
    osInfo = ""

    scanner = scan_object.scan_object()

    def __init__(self, address, scanBoolean):
        self.address = address
        self.portArray = []

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
            self.portArray.append(str(port_id))

        osmatch_elems = root.findall(".//osmatch")
        if len(osmatch_elems) > 0:
            self.osInfo = osmatch_elems[0].get('name')

    # adds the spam level to this object
    def readSpam(self):
        self.spamInfo = self.scanner.getSpamLevel(self.address)

    def readWhoIs(self):
        self.whoisInfo = self.scanner.getWhoIsData(self.address)

    def printPorts(self):
        return " PORTS: " + self.portInfo + "\n" 

    def getPortData(self, portNum):
        return "https://www.speedguide.net/port.php?port=" + str(portNum)

    def __str__(self):
        return "ADDR: " + self.address + "\n" + "ESTIMATED OS: " + self.osInfo + "\n" + "FRAUD LEVEL: " + self.spamInfo + "\n" + self.whoisInfo + "\n"


    

