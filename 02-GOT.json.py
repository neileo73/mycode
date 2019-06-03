#!/usr/bin/python3
"""Author: Neil Debah || Learning GOTjson.py"""

#pull in json lib so we can parse out json
import json

def main():
    # open the jonsnow.json file in read mode
    with open("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read()
        GOTpy = json.loads(jonsnow)
    print(GOTpy) #display te GOTpy data
    print(GOTpy["url"]) #dislay the value assoc. with URL
    print(GOTpy["titles"][0]) #display values assoc. with titles

    #create a loop to move across aliases
    with open("aliases.txt", "w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
            print(gotalias, file=jsaliases)


    print(GOTpy["aliases"]) #display values assoc with aliases
        #print(jonsnow["url'])

    # parse jonsnow.json file for...
    # display character alias / titles
    # display the API for ???





if __name__ == "__main__":
    main()
