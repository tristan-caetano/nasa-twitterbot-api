import requests
import request_tester as rt
import pprint
import webbrowser as wb
import PIL
import os
from PIL import Image
from datetime import date as dt

def download_picture(URL, title):

    image = requests.get(URL).content
    file = open(title + ".jpg", "wb")
    file.write(image)

    try:
        im = Image.open(title + ".jpg")
        im.show()
    except PIL.UnidentifiedImageError:
        print("File is not an image, deleting...")

        # This if else is redundant I know, don't yell at me
        if os.path.exists(title + ".jpg"):
            os.remove(title + ".jpg")
        else:
            print("Target file does not exist.")


    file.close()


def access_nasa():
    apikey = input("Please input your API key:\n ")

    url = "https://api.nasa.gov/planetary/apod?api_key=" + apikey
    epic_url = "https://epic.gsfc.nasa.gov/api/natural"
    check_access = rt.validateAccess(url)

    if check_access:
        return apikey
    else:
        return None

def apod():

    pp = pprint.PrettyPrinter()
    current_date = dt.today()


    URL_APOD = "https://api.nasa.gov/planetary/apod"
    current_date = current_date.strftime("%Y-%m-%d")
    params = {
          'api_key': access_nasa(),
          'date': current_date,
          'hd':'True'
      }

    response = requests.get(URL_APOD,params=params).json()

    print(response.get("title") +
    "\nDate: " + response.get("date") +
    "\n\n")
    pp.pprint(response.get("explanation"))
    print("\n\nURL: " + response.get("url"))

    if response.get("copyright") is not None:
        print("\nCopyright: " + response.get("copyright"))
    else:
        print("\nCopyright: None")

    download_picture(response.get("url"), response.get("title"))


apod()
