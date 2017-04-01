from flask import Flask , render_template,json,jsonify , request,redirect , url_for,session
import urllib.request
from urllib.request import urlopen


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def change():
    a=urllib.request.urlopen('http://api.fixer.io/latest')
    b=[]
    data=json.loads(a.read())

    for i in data['rates']:

        b.append(i)

    return render_template('index.html', b=b)

app.run()