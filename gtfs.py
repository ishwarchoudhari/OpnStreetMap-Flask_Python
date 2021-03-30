# Import related to GTFS
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
# Imports requests module
import requests
import time

gps_result = {}

def run():
    # Get gps data
    feed = gtfs_realtime_pb2.FeedMessage()

    # PMPML GTFS username and password
    username = "pmpmlgtfs"
    password = "7ry73auycBNTkC7m"

    response = requests.get('http://117.232.125.138/tms/data/gtfs/vehicle-positions.pb', auth=(username, password))
    feed.ParseFromString(response.content)
    feed = MessageToDict(feed)

    for entity in feed['entity']:
        data = entity['vehicle']['position']
        if entity['vehicle']['vehicle']['id'] == "ANT74":
            print(entity['vehicle']['vehicle']['id'], " = ", data)
            data.update({"route": entity['vehicle']['trip']['tripId']})
            gps_result.update({entity['vehicle']['vehicle']['id']: data})
            print(entity)


for i in range(1, 100):
    run()
    time.sleep(3)
