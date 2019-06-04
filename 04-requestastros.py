#!/usr/bin/python3
""" author: Neil Debah || Learning python """

import requests

MAJORTOM = "http://api.open-notify.orgz/astros.json"

def main():
    try:
        # make request
        pyj = requests.get(MAJORTOM).json()


        #parse out JSON we stripped off response
        astrocosmo = pyj.get("people")

        print("Currently in Space")
        for spaceperson in astrocosmo:
            print(spaceperson["name"])
    except:
        print("API is unavailable at the moment")
        exit()

if __name__ == "__main__":
    main()

