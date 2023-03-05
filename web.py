from flask import Flask, render_template, request
import scan_object
import host_object
import time
import os

app = Flask(__name__)
scanner = scan_object.scan_object()
hostList = []

#landing page
@app.route('/')
def hello():
    return render_template("index.html")
  

@app.route('/scan', methods = ['POST', 'GET']) 
def data():
    if request.method == "POST":

        scanner.iplist = []

        form_data = request.form.get('text_input')
        print("INPUTTED ADDRESS: " + form_data)


        tries = 0
        while len(scanner.iplist) == 0 or tries > 3:
                                    # 69.128.137.0/24
            scanner.scanAddressRange(str(form_data))
            tries = tries + 1

        global hostList
        hostList = []


        index = 0
        while index < len(scanner.iplist):
            if(os.path.exists('singles/' + str(scanner.iplist[index]) + ".xml") == False):
                print('scanning' +  str(scanner.iplist[index]))
                scanner.scanSingleAddress(scanner.iplist[index])
            
            hostList.append(host_object.host_object(scanner.iplist[index], True))
            index = index + 1

        return render_template("scan.html", form_data = hostList)

@app.route('/specific', methods = ['POST', 'GET']) 
def lookup():
    if request.method == "POST":

        portList = []
        form_data = request.form.get('port_input')

        for host in hostList:
            if str(form_data) in host.portArray:
                portList.append(host)

        return render_template("scan.html", form_data = portList)


if __name__ == "__main__":
    app.run()