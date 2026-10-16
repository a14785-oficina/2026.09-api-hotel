from flask_restful import Resource, reqparse

hotels = [
    { "hotel_id": "paradise", "name": "Paradise Hotel", "stars": 4.7, "daily": 123.99, "city": "Porto" },
    { "hotel_id": "fukui", "name": "Fukui Hotel", "stars": 4.3, "daily": 199.99, "city": "Viena" },
    { "hotel_id": "aqua", "name": "Aqua Hotel", "stars": 4.5, "daily": 149.99, "city": "Lisbon" },
]

# List all hotels
class Hotels(Resource):
    def get(self):
        return { "hotels": hotels }

# List, insert, update and delete a hotel in specific
class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument("name", type=str, required=True, help="The field 'name' cannot be left blank!")
    args.add_argument("stars", type=float, required=True, help="The field 'stars' cannot be left blank!")
    args.add_argument("daily", type=float, required=True, help="The field 'daily' cannot be left blank!")
    args.add_argument("city", type=str, required=True, help="The field 'city' cannot be left blank!")

    def get(self, id_hotel):
        for hotel in hotels:
            if hotel["hotel_id"] == id_hotel:
                return hotel, 200
        return { "message": "Hotel was not found!" }, 404

    def post(self, id_hotel):
        data = Hotel.args.parse_args() # Dictionary with the data sent in the request
        for hotel in hotels:
            if hotel["hotel_id"] == id_hotel:
                return { "message": f"Hotel '{id_hotel}' already exists!" }, 400

        new_hotel = { "hotel_id": id_hotel, **data }
        hotels.append(new_hotel)
        return { "message": f"Hotel '{id_hotel}' created successfully!" }, 200