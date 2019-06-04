#!/usr/bin/python3
""" author: Neil Debah || Learning python """

import json
import urllib.request

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    # make request
    resp = urllib.request.urlopen(MAJORTOM)
    # print(dir(resp)) # return the methods 
    # make python string JSON data FROM the 200 response
    jstring = resp.read()

    # convert string data to JSON
    #print(jstring)
    #print(type(jstring))
    #print(dir(jstring))
    pyj = json.loads(jstring.decode( 'utf-8' ))

    #parse out JSON we stripped off response
    astrocosmo = pyj.get("people")

    print("Currently in Space")
    for spaceperson in astrocosmo:
        print(spaceperson["name"])

    #display selected data on screen - names of people

if __name__ == "__main__":
    main()

