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

        self.new = {x['id']: Employee(x['userId'], x['username'], x['server'], x['rank']) for x in result['response']['staff']}
        
    def get_added(self):
        delta = self.new.keys() - self.old.keys()

        added = dict(filter(lambda x: x[0] in delta, self.new.items()))

        return added

    def get_updated(self):
        updated = {key: (self.old[key], self.new[key]) for key in self.old if key in self.new and self.old[key] != self.new[key]}

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
    import json

    result = json.loads(r'{"success":true,"status":"generic.ok","statuses":["generic.ok"],"response":{"staff":[{"id":799,"userId":"bff31e03-7f80-417c-8ef8-7900cd054017","username":"EHOT_fake","server":"Vanilla","rank":"Архитектор"},{"id":1,"userId":"0d8c3a84-cc60-372f-b9f8-dea7ce759c49","username":"MailGik","server":"Главные администраторы","rank":"Главный администратор"},{"id":16,"userId":"0ad0ef56-1ed8-388e-b79b-0721ecc4b1ad","username":"makkarpov","server":"Главные администраторы","rank":"Главный администратор"},{"id":19,"userId":"84cfc292-abe0-3700-8aad-4286421e2bbd","username":"Tentacle","server":"Главные администраторы","rank":"Главный администратор"},{"id":96,"userId":"fb1ad242-8dca-36de-9b1e-bf7344acd3f3","username":"dieKartoffel","server":"Magick","rank":"Помощник"},{"id":802,"userId":"d0bb0c87-671f-3248-9cfb-8ffc054cfd9f","username":"kileraz","server":"Magick","rank":"Помощник"},{"id":41,"userId":"0535bc09-8ff3-38c8-97a0-e57b98cde108","username":"SSKirillSS","server":"Magick","rank":"Администратор"},{"id":309,"userId":"918c1e5c-1631-3983-bbb4-419e9146e9f5","username":"_Description_","server":"Старшие администраторы","rank":"Старший администратор"},{"id":609,"userId":"4440b4b7-e35e-4879-b465-9a0b2698349f","username":"chernenko","server":"TFC","rank":"Мастер"},{"id":26,"userId":"12c3def0-d81f-357c-841b-2d324e05f98e","username":"HixOff","server":"Старшие администраторы","rank":"Старший администратор"},{"id":334,"userId":"b67d0ebf-acbe-345b-a54c-938e86d001a2","username":"isKONSTANTIN","server":"Старшие администраторы","rank":"Старший администратор"},{"id":412,"userId":"d0fe3c87-efef-4894-8be0-cf340edf7708","username":"CompWizard","server":"Minigames","rank":"Модератор"},{"id":632,"userId":"36fb7ded-eb26-35f5-960b-6e0314226e6a","username":"Rurla","server":"TFC","rank":"Администратор"},{"id":500,"userId":"a6c6dd90-e9ac-4bc5-9f0f-78abcb414e51","username":"pymi","server":"TFC","rank":"Управляющий"},{"id":641,"userId":"2e666510-f3e4-41d8-be0f-37d4a8848395","username":"KISKA_SOSISKA","server":"HiPower","rank":"Помощник-стажёр"},{"id":24,"userId":"36fb7ded-eb26-35f5-960b-6e0314226e6a","username":"Rurla","server":"Главные администраторы","rank":"Главный администратор"},{"id":67,"userId":"251f7ab3-f69e-3b12-b4db-5028f2988d81","username":"b4z3n","server":"HiTech","rank":"Управляющий"},{"id":678,"userId":"b67d0ebf-acbe-345b-a54c-938e86d001a2","username":"isKONSTANTIN","server":"Sandbox","rank":"Администратор"},{"id":670,"userId":"c4286dc4-918b-3bd2-a6ab-939f70b55e0d","username":"DimBot","server":"HiPower","rank":"Модератор"},{"id":673,"userId":"26c06304-f8a2-4785-933b-a59ef5e71522","username":"Nitka","server":"HiPower","rank":"Помощник"},{"id":680,"userId":"c47a37c2-9f8b-4add-82cd-2a2eac45740b","username":"Fire_Ball_20001","server":"HiPower","rank":"Модератор"},{"id":695,"userId":"e6299876-217f-3c35-bbc3-fcc423b7ac6f","username":"Hilarious","server":"Весь проект","rank":"Помощник"},{"id":722,"userId":"2afd410e-2e5b-33da-96f1-8513b2f72d0d","username":"b12","server":"Minigames","rank":"Администратор"},{"id":726,"userId":"12c3def0-d81f-357c-841b-2d324e05f98e","username":"HixOff","server":"HiTech","rank":"Администратор"},{"id":17,"userId":"57ea7f7a-e0b6-37a6-9919-4e3aa6c95f44","username":"harati","server":"Главные администраторы","rank":"Главный администратор"},{"id":741,"userId":"d7f4974c-8ca2-3319-86b9-89d70fd91eaa","username":"Semite","server":"TFC","rank":"Администратор"},{"id":736,"userId":"b976993f-7493-4c62-8dc5-5576141d456a","username":"HatsuneMiku007","server":"Весь проект","rank":"Строитель"},{"id":792,"userId":"1e1083bc-a8b1-4f47-b068-fead1e885eae","username":"Zayn","server":"Minigames","rank":"Помощник"},{"id":340,"userId":"8dd82a1e-1366-32ae-a4aa-0d8a859b0488","username":"iFhodx","server":"Magick","rank":"Управляющий"},{"id":760,"userId":"bff31e03-7f80-417c-8ef8-7900cd054017","username":"EHOT_fake","server":"Весь проект","rank":"Строитель"},{"id":766,"userId":"bff31e03-7f80-417c-8ef8-7900cd054017","username":"EHOT_fake","server":"HiPower","rank":"Строитель"},{"id":793,"userId":"0f62044a-04d5-31c8-abfe-e96c1cf850ee","username":"Tristaria","server":"HiPower","rank":"Помощник-стажёр"},{"id":368,"userId":"99819267-6b88-4977-8043-fdf25cd8db10","username":"Vebste","server":"Magick","rank":"Модератор"},{"id":441,"userId":"510b266b-4337-3cb8-8bcf-d7d3c044c903","username":"suslik","server":"HiPower","rank":"Управляющий"},{"id":774,"userId":"12c3def0-d81f-357c-841b-2d324e05f98e","username":"HixOff","server":"Sandbox","rank":"Администратор"},{"id":788,"userId":"51c06c52-73f4-355a-9d90-c6bac5d26f0f","username":"Nooky","server":"Minigames","rank":"Управляющий"},{"id":776,"userId":"24748b80-2974-4ebb-9bfd-1483de520fb3","username":"Volch0K","server":"HiTech","rank":"Модератор"},{"id":652,"userId":"78b29a07-8287-4ca7-89db-8124c3ed02b9","username":"leso","server":"HiPower","rank":"Помощник"},{"id":777,"userId":"b67d0ebf-acbe-345b-a54c-938e86d001a2","username":"isKONSTANTIN","server":"Sandbox","rank":"Управляющий"},{"id":781,"userId":"e6299876-217f-3c35-bbc3-fcc423b7ac6f","username":"Hilarious","server":"Весь проект","rank":"Никто"},{"id":794,"userId":"b67d0ebf-acbe-345b-a54c-938e86d001a2","username":"isKONSTANTIN","server":"Vanilla","rank":"Администратор"},{"id":797,"userId":"d68a32fd-b7c7-4c4a-b3ea-a92e51cc93eb","username":"DraAl","server":"Magick","rank":"Помощник"}]}}')

    tmp = {x['id']: Employee(x['userId'], x['username'], x['server'], x['rank']) for x in result['response']['staff']}

    with open("old.pickle", "wb") as file:
        pickle.dump(tmp, file)

    # staffList = StaffList()

    # print("   **Added**")
    # print(*[(x[0], x[1]) for x in staffList.get_added().values()], sep="\n")
    # print("   **Updated**")
    # print(*[(x[0], x[1]) for x in staffList.get_updated().values()], sep="\n")
    # print("   **Deleted**")
    # print(*[(x[0], x[1]) for x in staffList.get_deleted().values()], sep="\n")
