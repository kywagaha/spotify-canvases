import json
import re
import requests
import time
import sys

def askInfo(repeated):
    data = None
    try:
        f = open('canvases.json')
        data = json.load(f)
        f.close()
    except:
        print('')
        print('\033[91m\033[1mError\033[0m')
        print('File \033[1mcanvases.json\033[0m does not exist')
        print('')
        sys.exit(0)

    if repeated == False:
        print('')
        print(
            "Hi, thank you for contributing to \033[92m\033[1mspotify-canvases\033[0m!")
    else:
        print('')

    uri = input(
        "\033[1mPlease enter the track URI\033[0m › ")

    for urisInFile in data["canvases"]:
        if urisInFile["uri"] == uri:
            print('')
            print('\033[91m\033[1mError\033[0m')
            print('Track already exists in file')
            print('')
            repeat(True)

    songInfoReq = requests.get(
        'https://azx57uenaj.execute-api.us-west-1.amazonaws.com/production/getUriInfo', {'uri': uri})

    songInfo = songInfoReq.json()

    if songInfoReq.status_code == 200:
        songName = songInfo["message"]["name"]
        songArtist = songInfo["message"]["artists"][0]["name"]
        print('')
        print(f"""\033[1m{songName}\033[0m
{songArtist}""")
        print('')
        time.sleep(0.3)
        videoUrl = input(
            "\033[1mPlease enter the video URL\033[0m › ")
        addToJson(uri, songName, songArtist, videoUrl, repeated, data)
    else:
        print('')
        print('\033[91m\033[1mError\033[0m')
        print(songInfo["message"])
        print('')
        repeat(True)


def addToJson(uri, songName, songArtist, videoUrl, repeated, data):
    if bool(re.match(r"https:\/\/canvaz.scdn.co\/upload\/(artist||licensor)\/", videoUrl)) == False:
        print('')
        print('\033[91m\033[1mError\033[0m')
        print('Video URL is not a canvaz.scdn.co URL')
        print('')
        time.sleep(0.1)
        videoUrl = input(
            "\033[1mPlease enter the video URL\033[0m › ")
        addToJson(uri, songName, songArtist, videoUrl, repeated, data)   

    data['canvases'].append({
        "title": songName,
        "artist": songArtist,
        "uri": uri,
        "canvas": videoUrl
    })
    with open("canvases.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    print('')
    print("\033[92m\033[1mSuccessfully added!\033[0m")
    if repeated == False:
        print("Please make a pull request on the GitHub repository!")
    print('')
    repeat(False)


def repeat(error):
    if error:
        time.sleep(0.2)
        repeat = input("Would you like to try again? › [y/n] ")
        if repeat.lower() == "y" or repeat.lower == "yes":
            askInfo(True)
        else:
            sys.exit(0)
    else:
        time.sleep(0.1)
        repeat = input("Would you like to add another track? › [y/n] ")
        if repeat.lower() == "y" or repeat.lower == "yes":
            askInfo(True)
        else:
            sys.exit(0)


askInfo(False)
