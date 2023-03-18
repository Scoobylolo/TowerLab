#Author: Andy Carvajal    https://github.com/Scoobylolo

import requests
import sys
import location_api
import os

def get_info(mcc,mnc,lac,cell,what="city"):
    params = {
        "token": os.environ["CELLID"],
        "radio": "gsm",
        "mcc": mcc,
        "mnc": mnc,
        "lac": lac,
        "cell": cell,
    }

    url = "https://opencellid.org/cell/get?key={my_key}&mcc={mcc}&mnc={mnc}&lac={lac}&cellid={cellid}&format=json"
    url=url.format(my_key=params["token"],mcc=params["mcc"],mnc=params["mnc"],lac=params["lac"],cellid=params["cell"])

    response = requests.post(url, params=params)

    res=response.json()
    lat=res["lat"]
    lng=res["lon"]

    if what=="city":
        return location_api.get_city(lat,lng)
    return lat,lng

if __name__ == '__main__':
    lat,lng=get_info(310,410,54984,49024,what="latlng")
    print("Latitude:",lat)
    print("Longitude:",lng)

    what,where,country = location_api.get_city(lat,lng)

    print("{}: {}, {}".format(what,where,country))

