import requests
from collections import namedtuple
import pickle

Employee = namedtuple("Employee", ['userId', 'username', 'server', 'rank'])

if __name__ == "__main__":
    result = requests.get("https://api.hil.su/v2/staff/list").json()
    result = {x['id']: Employee(x['userId'], x['username'], x['server'], x['rank']) for x in result['response']['staff']}

    with open("old.pickle", "wb") as file:
        pickle.dump(result, file)
