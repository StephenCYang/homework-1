###################################
# IMPORT DEPENDENCIES
###################################

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import datetime as dt

from flask import Flask, jsonify

###################################
# DATABASE SETUP
###################################

# engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False}, echo=True)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement_table = Base.classes.measurement
station_table = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

###################################
# FLASK SETUP
###################################

app = Flask(__name__)


###################################
# FLASK ROUTES
###################################

# Page copy

@app.route("/")
def welcome():
    """List all available api routes."""
    return"""<html>
    <h1>Available API Routes for Honolulu Climate Analysis</h1>
    <ul>
    <br>
    <li>
    List of precipitations from last year:
    <br>
    <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a>
    </li>
    <br>
    <li>
    List of stations from the dataset: 
    <br>
   <a href="/api/v1.0/stations">/api/v1.0/stations</a>
   </li>
    <br>
    <li>
    List of Temperature Observations (tobs) for the previous year:
    <br>
    <a href="/api/v1.0/tobs">/api/v1.0/tobs</a>
    </li>
    <br>
    <li>
    List of TMIN, TAVG, and TMAX for the dates greater than or equal to the date provided:
    <br>Paste the string the string below to the URL above and replace the date desired in the proper format.
    <br>/api/v1.0/YYYY-MM-DD
    <br>
    <br>Hardcoded sample.
    <br>
    <a href="/api/v1.0/2010-01-01">/api/v1.0/2010-01-01</a>
    </li>
    <br>
    <li>
    List of TMIN, TAVG, and TMAX in between the dates provided:
    <br>Paste the string the string below to the URL above and replace the date range desired in the proper format.
    <br>/api/v1.0/YYYY-MM-DD/YYYY-MM-DD
    <br>
    <br>Hardcoded sample. 
    <br>
    <a href="/api/v1.0/2010-01-01/2010-01-31">/api/v1.0/2010-01-01/2010-01-31</a>
    </li>
    <br>
    </ul>
    </html>
    """

# Route: Precipitation
# ------------------------
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Docstring 
    """Return a list of precipitations from last year"""
    year_prior_date = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation = session.query(measurement_table.date, measurement_table.prcp).\
    filter(measurement_table.date >= year_prior_date).all()
    
    # Convert list of tuples into normal list
    precipitation_dict = dict(precipitation)

    return jsonify(precipitation_dict)

# Route: Stations
# ------------------------
@app.route("/api/v1.0/stations")
def stations(): 
    # Docstring
    """Return a JSON list of stations from the dataset."""
    # Query stations
    available_stations =  session.query(measurement_table.station).distinct().all()
    # Convert list of tuples into normal list
    stations_list = list(np.ravel(available_stations))

    return jsonify(stations_list)

# Route: TOBS
# ------------------------
@app.route("/api/v1.0/tobs")
def tobs(): 
    # Docstring
    """Return a JSON list of temperature observations (TOBS) for the previous year."""

    year_prior_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    # Query tobs
    most_active_station_data = session.query(measurement_table.tobs).\
        filter(measurement_table.station == "USC00519281").\
        filter(measurement_table.date >= year_prior_date).all()

    # Convert list of tuples into normal list
    tobs_list = list(np.ravel(most_active_station_data))

    return jsonify(tobs_list)

# Route: Start
# ------------------------
@app.route("/api/v1.0/<start>")
def start(start=None):

    # Docstring
    """Return a JSON list- calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date"""

    start_date = session.query(measurement_table.date, func.min(measurement_table.tobs), func.avg(measurement_table.tobs), func.max(measurement_table.tobs)).\
        filter(measurement_table.date >= start).group_by(measurement_table.date).all()
    start_date_list = list(start_date)
    # start_date_list = list(np.ravel(start_date))

    return jsonify(start_date_list)

# Route: Start/End
# ------------------------
@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    # Docstring
    """Return a JSON list- calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive."""
    
    between_dates = session.query(measurement_table.date, func.min(measurement_table.tobs), func.avg(measurement_table.tobs), func.max(measurement_table.tobs)).\
        filter(measurement_table.date >= start).filter(measurement_table.date <= end).group_by(measurement_table.date).all()
    between_dates_list = list(between_dates)
    # between_dates_list = list(np.ravel(between_dates))

    return jsonify(between_dates_list)


###################################
# DEFINE MAIN BEHAVIOR
###################################
if __name__ == '__main__':
    app.run(debug=True)