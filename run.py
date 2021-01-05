from app import app
from db import db

db.init_app(app)

# creats the data.db file, if it has not be created allready
@app.before_first_request
def create_tables():
    db.create_all()
