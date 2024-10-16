import requests
import os

CLIENT_ID=os.env.get('CLIENT_ID')



def get_device_code():
    url = 'https://github.com/login/device/code'
    paramters = {'client_id': CLIENT_ID}
    headers = {"Accept": "application/json"}
    x = requests.post(url, paramters, headers)
    device_code = x.text.split('&')[0].split('=')[1]
    print(device_code)
    return device_code

def get_token(devide_code):
    device_code = get_device_code()
    url = 'https://github.com/login/oauth/access_token'
    paramters = {"client_id": CLIENT_ID,
    "device_code": device_code,
    "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
    }
    headers = {"Accept":"application/json"}
    response = requests.post(url, paramters, headers)
    print(response.text)


devide_code=get_device_code()
get_token(devide_code)
