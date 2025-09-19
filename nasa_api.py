import requests
import request_tester as rt
import pprint
import webbrowser as wb
import PIL
import os
from PIL import Image
from datetime import date as dt
import pandas as pd
import re

# Def for downloading media from api request
def download_picture(title, URL):
    import re, os
    from PIL import Image
    import requests

    # Sanitize title for filename
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
    filename = f"{safe_title}.jpg"

    # Save image
    image = requests.get(URL).content
    with open(filename, "wb") as file:
        file.write(image)

    # Verify it's a valid image
    try:
        im = Image.open(filename)
        im.verify()  # Optional: verify image integrity
        return filename
    except (PIL.UnidentifiedImageError, IOError):
        print("File is not a valid image, deleting...")
        if os.path.exists(filename):
            os.remove(filename)
        return False

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
    list_of_params = [title, date, explanation[:200], url, copyright]

    try:
        # Printing info to console
        print(title +
        "\nDate: " + date +
        "\n\n")
        pp.pprint(explanation)
        print("\n\nURL: " + url)
    except:
        print("Nonetype in print.")

    # If there is no copyright, put None
    if response.get("copyright") is not None:
        print("\nCopyright: " + copyright)
    else:
        list_of_params[4] = "None"
        print("\nCopyright: None")

    # Returning info
    return list_of_params
    
