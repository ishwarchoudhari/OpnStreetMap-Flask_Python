import json
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

from flask import Flask, redirect, jsonify, url_for, session, escape, request
from flask import Flask, render_template, redirect, request, url_for, jsonify
import cgi
import jsonify
from google.transit import gtfs_realtime_pb2

from google.protobuf.json_format import MessageToDict
# Imports requests module

form = cgi.FieldStorage()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_map():
    return render_template('map.html')


@app.route('/getdata', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        Latitude = request.form['Latitude']
        Longitude = request.form['Longitude']
        ELatitude = request.form['ELatitude']
        ELongitude = request.form['ELongitude']
        print(" Start point Latitude:", Latitude)
        print(" Start point Longitude :", Longitude)
        print(" End point Latitude:", ELatitude)
        print(" End point Longitude:", ELongitude)
        return redirect(
            url_for('Map2', Latitude=Latitude, Longitude=Longitude, ELatitude=ELatitude, ELongitude=ELongitude))
    return render_template('Map2.html')

@app.route('/Map2')
def Map2():
    Latitude = request.args.get('Latitude', None)
    Longitude = request.args.get('Longitude', None)
    ELatitude = request.args.get('ELatitude', None)
    ELongitude = request.args.get('ELongitude', None)
    return render_template('Map2.html', Latitude=Latitude, Longitude=Longitude, ELatitude=ELatitude,
                           ELongitude=ELongitude)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)




