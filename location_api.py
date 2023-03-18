#Author: Andy Carvajal    https://github.com/Scoobylolo

import requests
import os


def get_city(lat, lng):
    # Set the API key and base URL

    url = 'https://api.radar.io/v1/geocode/reverse'
    params = {
        'coordinates': '{},{}'.format(lat, lng),
    }
    headers = {
        'Authorization': os.environ["GEOLOCATION"],
    }
    response = requests.get(url, params=params, headers=headers)
    json_object = response.json()
    # print(json_object)
    if response.status_code != 200:
        return None
    
    try:
        return "City",json_object["addresses"][0]["city"], json_object["addresses"][0]["country"]
    except KeyError:
        return "County",json_object["addresses"][0]["county"], json_object["addresses"][0]["country"]
    # print(json_object)

if __name__ == '__main__':
    what,where,country=get_city(27.912374,-99.958366)
    #The city at (37.7749, -122.4194) is San Francisco.
    print("{}: {}, {}".format(what,where,country))


