# sqlalchemy-challenge

Part 1: Analyze and Explore the Climate Data

In this section, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, I completed the following steps:

Use the SQLAlchemy create_engine() function to connect to your SQLite database.

Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Precipitation Analysis

Found the most recent date in the dataset.

Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.

Loaded the query results into a Pandas DataFrame, and set the index to the "date" column.

Plotted the results by using the DataFrame plot method, as the following image shows:

Used Pandas to print the summary statistics for the precipitation data using .descrbe().

Station Analysis

Designed a query to calculate the total number of stations in the dataset.

Designed a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

Listed the stations and observation counts in descending order.

Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

Filtered by the station that has the greatest number of observations.

Queried the previous 12 months of TOBS data for that station.

Plotted the results as a histogram with bins=12

Part 2: Designed a Climate App

Now that I’ve completed your initial analysis,I designed a Flask API based on the queries that I just developed. To do so, I used Flask to create your routes as follows:

Listed all the available routes:

/api/v1.0/precipitation

Converted the query results from your precipitation analysis to a dictionary using date as the key and prcp as the value.

Returned the JSON representation of your dictionary.

/api/v1.0/stations

Returned a JSON list of stations from the dataset.

/api/v1.0/tobs

Queried the dates and temperature observations of the most-active station for the previous year of data.

Returned a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>

Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

