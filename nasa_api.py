import requests
import request_tester as rt
import pprint
import webbrowser as wb
from PIL import Image


def access_nasa():
    apikey = "nBteOcB9TADPzVkGaLFEdd3S2fee6xOnbmwZe8T5"

    #apikey = input("Please input your api key for NASA: ")

    url = "https://api.nasa.gov/planetary/apod?api_key=" + apikey
    epic_url = "https://epic.gsfc.nasa.gov/api/natural"
    check_access = rt.validateAccess(url)

    if check_access:
        return apikey
    else:
        return None

def apod():

    pp = pprint.PrettyPrinter()

    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = '2020-01-22'
    params = {
          'api_key': access_nasa(),
          'date':date,
          'hd':'True'
      }

    response = requests.get(URL_APOD,params=params).json()

    download_picture(response.get("url"))

    print(response.get("title") +
    "\nDate: " + response.get("date") +
    "\n\n")
    pp.pprint(response.get("explanation"))
    print("\n\nURL: " + response.get("url") +
    "\nCopyright: " + response.get("copyright"))
    im.show()

    def download_picture(URL):

        binary = requests.get(URL).content
        file = open(response.get("title") + ".jpg", "wb")
        file.write(binary)
        im = Image.open("sample_image.jpg")
        file.close()


apod()
