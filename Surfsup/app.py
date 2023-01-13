# This script creates a Flask app that will display temperatature data from stations located in Hawaii

#Importimg Dependencies

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify    

#Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect an existing database into a new model
Base=automap_base()

Base.prepare(autoload_with=engine)

#Saving references to each table
measurement=Base.classes.measurement
stations=Base.classes.station

app = Flask(__name__)

#Displaying all routes that are available
@app.route('/')

def home():
    print('Server received request for "Home" page')
    return ('Welcome to my Home page!'
            'Available Routes:<br/>'
            '/api/v1.0/precipitation:<br/>'
            '/api/v1.0/stations:<br/>'
            '/api/v1.0/tobs:<br/>'
            '/api/v1.0/start (use yyyy-mm-dd format):<br/>'
            '/api/v1.0/start/end (use yyyy-mm-dd format):<br/>')

#Route displaying the precipitation data for the last year
@app.route('/api/v1.0/precipitation')
def precipitation():
    print('Server received request for "Precipitation" page')
    session = Session(engine)
    precipitation = session.query(measurement.date, measurement.prcp).filter(measurement.date>='2016-08-23').order_by(measurement.date).all()
    session.close()
    all_precipitation = []
    for date, prcp in precipitation:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)

#Route displaying the stations by name and station number
@app.route('/api/v1.0/stations')
def hawaii_stations():
    print('Server received request for "Stations" page')
    session=Session(engine)
    hawaii_stations=session.query(stations.station, stations.name).all()
    session.close()
    all_stations = []
    for station, name in hawaii_stations:
        stations_dict = {}
        stations_dict["station"] = station
        stations_dict["name"] = name
        all_stations.append(stations_dict)
    
    return jsonify(all_stations)

#Route displaying the temperature observations of the last year for the most active station (USC00519281)
@app.route('/api/v1.0/tobs')
def tobs():
    print('Server received request for "TOBS" page')
    session=Session(engine)
    busiest_station=session.query(measurement.date,measurement.tobs).filter(measurement.date>='2016-08-23').filter(measurement.station=='USC00519281').order_by(measurement.date).all()
    session.close()
    busy_temp_readings = []
    for date, tobs in busiest_station:
        busy_temp_dict = {}
        busy_temp_dict["date"] = date
        busy_temp_dict["tobs"] = tobs
        busy_temp_readings.append(busy_temp_dict)

    return jsonify(busy_temp_readings)

#Creating a variable to hold the minimum, maximum, and average temperature for the next two routes
select=[func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)]

#Route displaying the minimum, maximum, and average temperature for a given start date using the YYYY-MM-DD format
@app.route('/api/v1.0/<start>')
def starting_date(start):
    print('Server received request for "Start" page')
    session=Session(engine)
    start_date=session.query(*select).filter(measurement.date>=start).all()
    session.close()
    start_min_max_avg = []
    for min, max, avg in start_date:
        start_dict = {}
        start_dict["min"] = min
        start_dict["max"] = max
        start_dict["avg"] = avg
        start_min_max_avg.append(start_dict)

    return jsonify(start_min_max_avg)

#Route displaying the minimum, maximum, and average temperature for a given start & end date using the YYYY-MM-DD format
@app.route('/api/v1.0/<start>/<end>')
def start_end_date(start,end):
    print('Server received request for "Start/End" page')
    session=Session(engine)
    start_end=session.query(*select).filter(measurement.date>=start)\
       .filter(measurement.date<=end).all()
    session.close()
    start_end_min_max_avg = []
    for min, max, avg in start_end:
        start_end_dict = {}
        start_end_dict["min"] = min
        start_end_dict["max"] = max
        start_end_dict["avg"] = avg
        start_end_min_max_avg.append(start_end_dict)

    return jsonify(start_end_min_max_avg)
 
    
if __name__ == "__main__":
    app.run(debug=True)
