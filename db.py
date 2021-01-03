from flask_sqlalchemy import SQLAlchemy

# this is an object that will link to our flask app.
# it will look at the object we tell it to and map them to row in a database
db = SQLAlchemy()
