# -*- coding:utf8 -*-

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

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
app.config['DEBUG'] = True


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # # print(res)
    # r = make_response(res)
    # r.headers['Content-Type'] = 'application/json'
#     return r
    return None

# def processRequest(req):
#     if req.get("result").get("action") != "worldweatheronlineAPI":
#         return {}
#     baseurl = "https://api.worldweatheronline.com/premium/v1/weather.ashx?format=json&num_of_days=1"
#     wwoApiKey = "0ccfbc9eb3ab43d0a34120015181202"
#     yql_query = makeYqlQuery(req)
#     if yql_query is None:
#         return {}
#     yql_url = baseurl + urlencode({'q': yql_query}) + '&key=' + wwoApiKey + '&date=' + date + '&lang=ru'
#     print('Yql_url: '  + yql_url)
#     result = urlopen(yql_url).read()
#     data = json.loads(result)
#     # print('Data: ' + data)
#     res = makeWebhookResult(data)
#     return res


# def makeYqlQuery(req):
#     result = req.get("result")
#     parameters = result.get("parameters")
#     city = parameters.get("geo-city")
#     if city is None:
#         return None

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

#     speech = "Today the weather in " + location.get('city') + ": " + condition.get('text') + \
#              ", And the temperature is " + condition.get('temp') + " " + units.get('temperature')

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
