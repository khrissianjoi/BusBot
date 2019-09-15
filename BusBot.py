import requests
import os


import env_secrets

link = os.environ.get('BusLink')

ERROR_MESSAGES = ['Sorry human realtime information is currently unavailable', 'Sorry human, please enter a real bus stop number']
def get_stop_number():
    return  str(input('please enter the stop number\n'))


def get_request(current):
    '''returns json format and status code as a tuple'''
    request = requests.get(link, params=current)
    if request.status_code != 200:
        return ERROR_MESSAGES[0]
    request_json = request.json()
    if request_json['errormessage'] == 'No Results':
        return ERROR_MESSAGES[1]
    return request_json, request.status_code

def main():
    stop_id = get_stop_number()

    current = {
        'stopid' : stop_id, 
        'format' :'json'
    }

    response_json = get_request(current)
    if type(response_json) == tuple:
        for bus in response_json[0]['results']:
            print(bus['route'] +' ' + bus['duetime'])
    else:
        print(response_json)
main()