from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hotels
from con_sql import bd

# Variable representing the Flask application
app = Flask(__name__)

# Variable representing the Flask-RESTful API
api = Api(app)

# Configurations for the database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hotels.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Route for the Hotels resource
api.add_resource(Hotels, "/hotels")
api.add_resource(Hotel, "/hotels/<string:id_hotel>")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)