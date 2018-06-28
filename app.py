from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#Wetterdaten fuer Bonn und Darmstadt
darmstadt =    {
    "Darmstadt": {
        "Grad": 22,
        "Desc": "ohjjeee isch des heisss"
    }
}

bonn = {
    "Bonn": {
        "Grad": 43,
        "Desc": "grrrrr isch des kaaalt",
    }
}

weather = [{"Wetterdaten": {
    "Darmstadt": {
        "Grad": 22,
        "Desc": "ohjjeee isch des heisss",
           },
    "Bonn": {
        "Grad": 43,
        "Desc": "grrrrr isch des kaaalt",
    },
        }
}
]
#AUSGABE BROWSER
@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'GET':
        return render_template('index.html')
        city = request.form['city']
        return render_template('city.html', city=city)
'''
else:
     res.status_code == '200'
        res = requests.get('http://127.0.0.1:5000/send?q=Darmstadt')
        darmstadt = res.json()
           print(darmstadt)
           break
'''
if __name__ == "__main__":
        app.run()
