# repo-api-tester
Just having some fun with APIs

## What is the purpose of this repo?
REV1: Just a small project to learn about APIs, plus accessing NASA's API is kinda dope. I do have my own API key and will not supply it with the code, hence the input for it. However, the main project is technically the request_tester as it can tell you if you have access to a requested API, and if it contains the error code it will display it for you.
REV2: It's now a twitterbot that tweets nasa data every day.

## What do the scripts do?
The request_tester will take in a URL, usually containing the API key, and will print out an status code based on the connectivity to the API. There are 7 distict codes, however, if you run into a code that isnt there, it still knows the code range. IE: Is it a 300 level code and so on. It then returns a boolean depending on the success of the request.
The nasa_api accesses NASA's API and displays some info from their APOD website. If the request links to a picture, the script will download it.
The tweeter_api grabs the title, date, media link, and credit from the nasa api response and tweets it daily at noon.
The script is currently running off of a Raspberry Pi.

[Link to TwitterBot Page](https://twitter.com/SpaceBotBoi)
