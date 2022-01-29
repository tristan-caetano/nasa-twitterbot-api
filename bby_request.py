#import env
from email import header
import requests
import pandas as pd
from selenium import webdriver
import webbrowser
import request_tester as rt
from bs4 import BeautifulSoup
import os

options = webdriver.ChromeOptions()
options.binary_location = r"/usr/bin/google-chrome"
chrome_driver_binary = r"chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
print("Going to website")
driver.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440')
print("Finding button")
button = driver.find_element_by_id('data-button-state')



# print(os.path.exists("/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
# driver = webdriver
# driver.ChromeOptions().binary_location = "/usr/bin/google-chrome"
# driver = webdriver.Chrome(executable_path = "chromedriver")
# print("Going to website")
# driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
# print("Finding button")
# button = driver.find_element_by_id('data-button-state')
# print(button)


















# URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

# #rt.validateAccess(URL)

# req = requests.get(URL, headers = headers)
# content = req.text

# soup = BeautifulSoup(content)



# raw = soup.next_element('data-button-state')

# print(raw)

#print(req.content)

# print(content)

# headers = {
# 	'authority': 'www.bestbuy.ca',
# 	'pragma': 'no-cache',
# 	'cache-control': 'no-cache',
# 	'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4159.2 Safari/537.36',
# 	'accept': '*/*',
# 	'sec-fetch-site': 'same-origin',
# 	'sec-fetch-mode': 'cors',
# 	'sec-fetch-dest': 'empty',
# 	'referer': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440',
# 	'accept-language': 'en-US,en;q=0.9'

    
# }

# def main():
#     quantity = 0
#     attempt = 0

#     while (quantity < 1):
#         response = requests.get(URL, headers=headers)
#         response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

#         quantity = response_formatted['availabilities'][0]['shipping']['quantityRemaining']

#         if (quantity < 1):
#             #Out Of stock
#             print('Time=' + str(datetime.now()) + "- Attempt=" + str(attempt))
#             attempt += 1
#             time.sleep(5)
#         else:
#             print('Hey its in stock! Quantity=' + str(quantity))
#             #publish(quantity)


# def publish(quantity):
#     arn = 'arn:aws:sns:us-east-1:398447858632:InStockTopic'
#     sns_client = boto3.client(
#         'sns',
#         aws_access_key_id=env.accessKey,
#         aws_secret_access_key=env.secretKey,
#         region_name='us-east-1'
#     )

#     response = sns_client.publish(TopicArn=arn, Message='Its in stock! Quantity=' + str(quantity))
#     print(response)

# main()