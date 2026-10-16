from flask import Flask
from flask_restful import Api
from resources.hotel import Hotel, Hotels

# Variable representing the Flask application
app = Flask(__name__)

# Variable representing the Flask-RESTful API
api = Api(app)

# Route for the Hotels resource
api.add_resource(Hotels, "/hotels")
api.add_resource(Hotel, "/hotels/<string:id_hotel>")

if __name__ == "__main__":
    app.run(debug=True)