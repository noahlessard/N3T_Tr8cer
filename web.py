from flask import Flask, render_template, request
import scan_object
import host_object
import time

app = Flask(__name__)
scanner = scan_object.scan_object()

#landing page
@app.route('/')
def hello():
    return render_template("index.html")
  
#this will be where the app will route when the HQ images is actually needed
@app.route('/hd/')
def about():
    return render_template("")

@app.route('/scan', methods = ['POST', 'GET']) 
def data():
    if request.method == "POST":
        form_data = request.form.get('text_input')
        time.sleep(2)


        sampledata = []
        sampledata.append(host_object.host_object("69.128.137.0", False))
        sampledata.append(host_object.host_object("69.128.137.1", False))
        sampledata.append(host_object.host_object("69.128.137.2", False))                
        
        return render_template("scan.html", form_data = sampledata)

if __name__ == "__main__":
    app.run()