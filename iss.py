import requests
import json
import time

__author__ = 'Billy Yip with Alex Mourtos helping with Part C'


def astronaunts():
    astronaut_API = requests.get('http://api.open-notify.org/astros.json')
    astronaut_data = astronaut_API.text
    parse_astronaut = json.loads(astronaut_data)
    problem_a = parse_astronaut['people']
    print(
        "There are {} astronaunts in space.".format(parse_astronaut['number']))
    for a in range(len(problem_a)):
        print(
            "{} is on craft {}.\
                ".format(problem_a[a]['name'], problem_a[a]['craft']))


def spacestation():
    API_fetch = requests.get('http://api.open-notify.org/iss-now.json')
    API_data = API_fetch.text
    parse_data = json.loads(API_data)
    times = parse_data['timestamp']
    latitude = parse_data['iss_position']['latitude']
    longitude = parse_data['iss_position']['longitude']
    print(
        "Station is at coordinates: {}, {} at this time: {}.".format(
            latitude, longitude, times))


def hover_over():
    coordinates = {'lat': '40.273502', "lon": '-86.126976'}
    fetch = requests.get(
        'http://api.open-notify.org/iss-pass.json', params=coordinates)
    data = fetch.text
    parse_data = json.loads(data)
    testing = parse_data['response']
    # times = parse_data['response'][0]['risetime']
    # print(parse_data)
    # passover = time.ctime(times)
    for t in range(len(testing)):
        print(
            "The station will passe over Indianapolis, Indiana on: ",
            time.ctime(parse_data['response'][t]['risetime']))
    # test = print(time.ctime(parse_data['response']['risetime']))
    # print(test)
    # print(
    #     "The station will passe over Indianapolis, Indiana on: {}.".format(
    #         passover))


def main():
    astronaunts()
    spacestation()
    hover_over()


if __name__ == '__main__':
    main()
