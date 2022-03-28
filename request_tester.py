import requests

# Simply getting request codes
def validateAccess(url):

    # Sent api info
    api = requests.get(url)

    # Declaring return statement
    can_advance = False

    # Notifying that its checking for api codes
    print("Checking Request for URL: " + url)

    # If else statements for general status codes
    if (api.status_code > 199) and (api.status_code < 300):
        print("Success: ", end = '')
        can_advance = True
    elif (api.status_code > 299) and (api.status_code < 400):
        print("Redirect: ", end = '')
    elif (api.status_code > 399) and (api.status_code < 500):
        print("Bad Request: ", end = '')
    elif (api.status_code > 499) and (api.status_code < 600):
        print("Internal Server Error: ", end = '')
    else:
        print("Error Code out of Range: ", end = '')

    # Printing actual status code
    print(api.status_code)

    # Printing specific common status codes
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

    print("\n")

    # Returning true if 200 level code
    return(can_advance)
