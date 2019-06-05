#!/usr/bin/python3

""" author: Neil Debah || learning about nasa APIs and dev keys """

import requests

MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="

def keyharvester():
    with open("/home/student/nasa.key", "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')

def main():
    # harvest our key from /home/student/nasa.key
    nasakey = keyharvester()

    print(nasakey)
    # append our key to MYAPI
    # call the API (request.get()) and pull off json (.json())
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()
    print(asteroidz)    
    #parse json - loop across "near_earth_objects" to reveal astroids
    for bigrock in asteroidz["near_earth_objects"]:
        if bigrock["is_potentially_hazardous_asteroid"]:
            print("name - ", bigrock["name"])
            print("Promimity - ", bigrock["close_approach_data"])
            print("Size - ", bigrock["estimated_diameter"], end="\n***************\n")
        else:
            print("This asteroid is not one to concern yourself with")


if __name__ == "__main__":
    main()
