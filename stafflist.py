import requests
from collections import namedtuple
import pickle

Employee = namedtuple("Employee", ['userId', 'username', 'server', 'rank'])


class StaffList:
    # old = {794: Employee(usedId='b67d0ebf-acbe-345b-a54c-938e86d001a2', username='isKONSTANTIN', server='Vanilla', rank='Администратор'), 1337: Employee(usedId='', username='CompWizard', server='Minigames', rank='Главный администратор'), 888: Employee(usedId='', username='harati', server='All', rank='All')}
    old = {}
    new = {}

    def __init__(self, file_name="old.pickle"):
        self.file_name = file_name

        try:
            with open(self.file_name, "rb") as file:
                self.old = pickle.load(file)
        except:
            print("No such file")
            exit(0)

        self.update()

    def update(self):
        try:
            result = requests.get("https://api.hil.su/v2/staff/list").json()
        except Exception as x:
            print(x)
            return

        if result['success'] != True:
            return

        self.new = {x['id']: Employee(
            x['userId'], x['username'], x['server'], x['rank']) for x in result['response']['staff']}

    def get_added(self):
        delta = self.new.keys() - self.old.keys()

        added = dict(filter(lambda x: x[0] in delta, self.new.items()))

        return added

    def get_updated(self):
        updated = {key: (self.old[key], self.new[key])
                   for key in self.old if key in self.new and self.old[key] != self.new[key]}

        return updated

    def get_deleted(self):
        delta = self.old.keys() - self.new.keys()

        deleted = dict(filter(lambda x: x[0] in delta, self.old.items()))

        return deleted

    def save(self):
        self.old = self.new

        with open(self.file_name, "wb") as file:
            pickle.dump(self.old, file)


if __name__ == "__main__":
    pass
