from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

import urllib.parse

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "worldweatheronlineAPI":
        return {}
    baseurl = "http://api.worldweatheronline.com"
    wwoApiKey = "0ccfbc9eb3ab43d0a34120015181202"

    result = req.get("result")
    print('Result: ' + result)
    parameters = result.get("parameters")
    print('Parameters: ' + parameters)
    city = parameters.get("geo-city")
    if city is None:
        return None
    if parameters.get("date"):
        date = parameters.get("date")

    callWeatherApi(city, date, baseurl,wwoApiKey)

    speech = "погода"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


def callWeatherApi(city, date, baseurl, wwoApiKey):
    path = '/premium/v1/weather.ashx?format=json&num_of_days=1' + '&q=' + urllib.parse.quote(city.encode("utf-8")) + '&key=' + wwoApiKey + '&date=' + date + '&lang=ru'
    print('API Request: ' + baseurl + path)
    url = baseurl + path
    result = urlopen(url).read()
    print('Result request: ' + result)
#    data = json.loads(result)
#    res = makeWebhookResult(data)
#    return res


# def itsm365Weather(req):
#     result = req.get("result")
#     print(result)
#     parameters = result.get("parameters")
#     print("------------")
#     print(parameters)
#     city = parameters.get("address")
#     if city is None:
#         return None
#     if parameters.get("date"):
#         date = parameters.get("date")

#     return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


# def makeWebhookResult(data):
#     query = data.get('query')
#     if query is None:
#         return {}

#     result = query.get('results')
#     if result is None:
#         return {}

#     channel = result.get('channel')
#     if channel is None:
#         return {}

#     item = channel.get('item')
#     location = channel.get('location')
#     units = channel.get('units')
#     if (location is None) or (item is None) or (units is None):
#         return {}

#     condition = item.get('condition')
#     if condition is None:
#         return {}

#     # print(json.dumps(item, indent=4))

#     speech = "Сегодня погода в " + location.get('city') + ": " + condition.get('text') + \
#              ", И температура " + condition.get('temp') + " " + units.get('temperature')

#     print("Response:")
#     print(speech)

#     return {
#         "speech": speech,
#         "displayText": speech,
#         # "data": data,
#         # "contextOut": [],
#         "source": "apiai-weather-webhook-sample"
#     }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
