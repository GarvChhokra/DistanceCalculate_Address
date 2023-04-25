from flask import Flask, request, jsonify
from geopy.distance import geodesic
from flask_cors import CORS
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="my app")

CORS(app)


@app.route('/distance/<address1>/<address2>', methods=['GET'])
def get_distance(address1, address2):
    location_1 = geolocator.geocode(address1)
    location_2 = geolocator.geocode(address2)

    if location_1 is None or location_2 is None:
        return jsonify({'error': 'Unable to geocode addresses'}), 400

    lat_1, lon_1 = location_1.latitude, location_1.longitude
    lat_2, lon_2 = location_2.latitude, location_2.longitude

    distance = geodesic((lat_1, lon_1), (lat_2, lon_2)).km

    return jsonify({'distance_km': distance})


if __name__ == '__main__':
    app.run(debug=True)
