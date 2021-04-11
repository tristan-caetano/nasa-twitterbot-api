import requests

def validateAccess(url):

    api = requests.get(url)

    if (api.status_code > 199) and (api.status_code < 300):
        print("Success: ", end = '')
    elif (api.status_code > 299) and (api.status_code < 400):
        print("Redirect: ", end = '')
    elif (api.status_code > 399) and (api.status_code < 500):
        print("Bad Request: ", end = '')
    elif (api.status_code > 499) and (api.status_code < 600):
        print("Internal Server Error: ", end = '')
    else:
        print("Error Code out of Range: ", end = '')
        
    print(api.status_code)

    if api.status_code == 200: 
        print("Access Granted")
    elif api.status_code == 301:
        print("Redirecting")
    elif api.status_code == 400:
        print("Bad Request")
    elif api.status_code == 401:
        print("Not Authenticated")
    elif api.status_code == 403:
        print("Forbidden")
    elif api.status_code == 404:
        print("Not Found")
    elif api.status_code == 503:
        print("Server Cannot Handle Request")
    