from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#Wetterdaten fuer Bonn und Darmstadt

weather = {
    "Bonn": {
        "Grad": 43,
        "Desc": "grrrrr isch des kaaalt",
    },
    "Darmstadt": {
            "Grad": 22,
            "Desc": "ohjjeee isch des heisss"
    }
}

#AUSGABE BROWSER
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/city', methods=['GET','POST'])
def city():
    city = request.args.get('q')

    try:
        content = weather[city]
    except Exception as e:
        return render_template('error.html', error="City not found")

    acceptHeader = request.headers.get('Accept')

    if acceptHeader.startswith( 'text/html' ):
        return render_template('city.html', forecast=content['Desc'], temp=content['Grad'])

    if acceptHeader.startswith( 'application/json' ):
        return jsonify(content)

    return render_template('city.html', city=city)

if __name__ == "__main__":
    app.run(debug=True)
