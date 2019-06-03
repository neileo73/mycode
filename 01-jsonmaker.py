#!/usr/bin/python3
'''Author: Neil Debah | Email: ndebah@optonline.net || Learning JSON'''

# with python, the json batteries is in the box, but you need to plug them in
import json

def main():
    videogames = [{"game1": "pacman", "game2": "centepede", "game3": "donkey kong", "game4": "turbo"}, {"game1": "ms  pacman", "game2": "paperboy"}]

    # show the values of videogames
    print(videogames)

    # create a local file
    with open("videogames.json", "w") as vidfile: # "w" = write, "r" = read, "a" = append
        json.dump(videogames, vidfile)

if __name__ == "__main__":
    main()


