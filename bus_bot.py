import requests
import os


import secrets

link = os.environ.get('BUS_LINK')

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
# result = {"errorcode":"0","errormessage":"","numberofresults":8,"stopid":"4793","timestamp":"25\/06\/2019 20:00:32","results":[{"arrivaldatetime":"25\/06\/2019 20:01:18","duetime":"Due","departuredatetime":"25\/06\/2019 20:01:18","departureduetime":"Due","scheduledarrivaldatetime":"25\/06\/2019 20:00:00","scheduleddeparturedatetime":"25\/06\/2019 20:00:00","destination":"Broombridge Luas","destinationlocalized":"Broombridge Luas","origin":"Tyrrelstown","originlocalized":"Baile an Tirialaigh","direction":"Inbound","operator":"bac","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"40E","sourcetimestamp":"25\/06\/2019 19:51:33","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:16:00","duetime":"15","departuredatetime":"25\/06\/2019 20:16:00","departureduetime":"15","scheduledarrivaldatetime":"25\/06\/2019 20:16:00","scheduleddeparturedatetime":"25\/06\/2019 20:16:00","destination":"Howth Junction","destinationlocalized":"Prd Chill Bharróg","origin":"Blanchardstown","originlocalized":"Baile Bhlainséir","direction":"Inbound","operator":"GAD","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"17A","sourcetimestamp":"25\/06\/2019 19:56:31","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:29:32","duetime":"28","departuredatetime":"25\/06\/2019 20:29:32","departureduetime":"28","scheduledarrivaldatetime":"25\/06\/2019 20:30:00","scheduleddeparturedatetime":"25\/06\/2019 20:30:00","destination":"Broombridge Luas","destinationlocalized":"Broombridge Luas","origin":"Tyrrelstown","originlocalized":"Baile an Tirialaigh","direction":"Inbound","operator":"bac","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"40E","sourcetimestamp":"25\/06\/2019 19:30:06","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:34:00","duetime":"33","departuredatetime":"25\/06\/2019 20:34:00","departureduetime":"33","scheduledarrivaldatetime":"25\/06\/2019 20:34:00","scheduleddeparturedatetime":"25\/06\/2019 20:34:00","destination":"DCU","destinationlocalized":"DCU","origin":"Lady's Well Road","originlocalized":"Lady's Well Road","direction":"Inbound","operator":"GAD","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"220","sourcetimestamp":"25\/06\/2019 19:51:33","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:34:00","duetime":"33","departuredatetime":"25\/06\/2019 20:34:00","departureduetime":"33","scheduledarrivaldatetime":"25\/06\/2019 20:34:00","scheduleddeparturedatetime":"25\/06\/2019 20:34:00","destination":"Howth Junction","destinationlocalized":"Prd Chill Bharróg","origin":"Blanchardstown","originlocalized":"Baile Bhlainséir","direction":"Inbound","operator":"GAD","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"17A","sourcetimestamp":"25\/06\/2019 19:49:54","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:45:16","duetime":"44","departuredatetime":"25\/06\/2019 20:45:16","departureduetime":"44","scheduledarrivaldatetime":"25\/06\/2019 20:45:00","scheduleddeparturedatetime":"25\/06\/2019 20:45:00","destination":"Parnell St","destinationlocalized":"Sráid Parnell","origin":"Tyrrelstown","originlocalized":"Baile an Tirialaigh","direction":"Inbound","operator":"bac","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"40D","sourcetimestamp":"25\/06\/2019 19:46:36","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:54:00","duetime":"53","departuredatetime":"25\/06\/2019 20:54:00","departureduetime":"53","scheduledarrivaldatetime":"25\/06\/2019 20:54:00","scheduleddeparturedatetime":"25\/06\/2019 20:54:00","destination":"Howth Junction","destinationlocalized":"Prd Chill Bharróg","origin":"Blanchardstown","originlocalized":"Baile Bhlainséir","direction":"Inbound","operator":"GAD","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"17A","sourcetimestamp":"25\/06\/2019 19:54:52","monitored":"true"},{"arrivaldatetime":"25\/06\/2019 20:59:05","duetime":"58","departuredatetime":"25\/06\/2019 20:59:05","departureduetime":"58","scheduledarrivaldatetime":"25\/06\/2019 20:59:00","scheduleddeparturedatetime":"25\/06\/2019 20:59:00","destination":"Broombridge Luas","destinationlocalized":"Broombridge Luas","origin":"Tyrrelstown","originlocalized":"Baile an Tirialaigh","direction":"Inbound","operator":"bac","operatortype":"1","additionalinformation":"","lowfloorstatus":"no","route":"40E","sourcetimestamp":"25\/06\/2019 19:59:49","monitored":"true"}]}