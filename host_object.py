import xml.etree.ElementTree as ET
import scan_object


class host_object:
    # this will all stay public so don't worry about setters
    whoisInfo = ""
    portInfo = []
    spamInfo = ""
    address = ""

    scanner = scan_object.scan_object()

    def __init__(self, address):
        host_object.address = address
        return 

    # adds ports from nmap xml file to this object
    def readXML(self):
        tree = ET.parse('singles/' + self.address + '.xml')
        root = tree.getroot()
        for port in root.findall('.//port'):
            port_id = port.get('portid')
            self.portInfo.append(port_id)

    # adds the spam level to this object
    def readSpam(self):
        self.spamInfo = self.scanner.getSpamLevel(self.address)

    def readWhoIs(self):
        self.whoisInfo = self.scanner.getWhoIsData(self.address)

    

    

