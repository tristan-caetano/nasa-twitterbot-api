import requests
import request_tester as rt
import pprint
import webbrowser as wb
import PIL
import os
from PIL import Image
from datetime import date as dt
import pandas as pd

# Def for downloading media from api request
def download_picture(URL, title):

    # Getting image content
    image = requests.get(URL).content

    # Saving image as a .jpg
    file = open(title + ".jpg", "wb")
    file.write(image)

    # Try catch to make sure the media is a downloadable image
    try:
        im = Image.open(title + ".jpg")
        im.show()
    except PIL.UnidentifiedImageError:
        print("File is not an image, deleting...")

        # This if else is redundant
        if os.path.exists(title + ".jpg"):
            os.remove(title + ".jpg")
        else:
            print("Target file does not exist.")

    # Closing file to prevent data leak
    file.close()

# Getting required api info
def access_nasa():

    # Getting api key (not included in repo)
    keys = pd.read_csv('keys.csv')
    apikey = keys['nasa'][0]

    # Making sure access is granted
    url = "https://api.nasa.gov/planetary/apod?api_key=" + apikey
    epic_url = "https://epic.gsfc.nasa.gov/api/natural"
    check_access = rt.validateAccess(url)

    # Respective return depending on access code
    if check_access:
        return apikey
    else:
        return None

# Main API interfacer
def apod():

    # Setting up printer to get pictures
    pp = pprint.PrettyPrinter()

    # Getting todays date info
    current_date = dt.today()

    # Setting up url
    URL_APOD = "https://api.nasa.gov/planetary/apod"

    # Getting basic date info
    current_date = current_date.strftime("%Y-%m-%d")

    # Filling parameters for api
    params = {
          'api_key': access_nasa(),
          'date': current_date,
          'hd':'True'
      }

    # Getting request
    response = requests.get(URL_APOD,params=params).json()

    # Extracting all needed info
    title = response.get("title")
    date = response.get("date")
    explanation = response.get("explanation")
    url = response.get("url")
    copyright = response.get("copyright")

    # Creating a list of into to send to twitter api
    list_of_params = [title, date, explanation, url, copyright]

    # Printing info to console
    print(title +
    "\nDate: " + date +
    "\n\n")
    pp.pprint(explanation)
    print("\n\nURL: " + url)

    # If there is no copyright, put None
    if response.get("copyright") is not None:
        print("\nCopyright: " + copyright)
    else:
        list_of_params[4] = "None"
        print("\nCopyright: None")

    # Downloads picture to local dir
    # download_picture(response.get("url"), response.get("title"))

    # Returning info
    return list_of_params
    
