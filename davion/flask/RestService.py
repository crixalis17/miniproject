from flask import Flask, jsonify;
from flask_cors import CORS;
# from flask_restful import Resource, Api;


app = Flask(__name__)
# api=Api(app)
CORS(app)

weather = {
    "data": [
    {
        "day": "1/6/2019",
        "temperature": "23",
        "windspeed": "16",
        "event": "Sunny"
    },
    {
        "day": "2/6/2019",
        "temperature": "21",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "3/6/2019",
        "temperature": "31",
        "windspeed": "12",
        "event": "Sunny"
    },
    {
        "day": "4/6/2019",
        "temperature": "5",
        "windspeed": "28",
        "event": "Snow"
    },
    {
        "day": "5/6/2019",
        "temperature": "17",
        "windspeed": "18",
        "event": "Rainy"
    },
    {
        "day": "6/6/2019",
        "temperature": "19",
        "windspeed": "21",
        "event": "Rainy"
    },
    {
        "day": "7/6/2019",
        "temperature": "28",
        "windspeed": "14",
        "event": "Sunny"
    }
    ]
}


@app.route("/", methods=['GET'])
def index():
    return "Welcome to CodezUp";

@app.route("/weatherReport/", methods = ['GET'])
def WeatherReport():
    global weather
    return jsonify([weather])

if __name__ == '__main__':
    app.run(debug=True)
