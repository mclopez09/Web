from repositories.PersonsRepository import PersonsRepository

class PersonsService(object):
    def __init__(self):
        self.Persons_repository = PersonsRepository()

    def add_Person(self, name):
        return self.Persons_repository.add_Person(name)

    def get_all_Persons(self, page, pagesize, name):
        print("...service....name: " +name)
        return self.Persons_repository.get_all_Persons(page, pagesize, name)

    def get_Person_by_id(self, id):
        return self.Persons_repository.get_Person_by_id(id)

    def update_Person(self, id, name):
        return self.Persons_repository.update_Person(id, name)

    def delete_Person(self, id):
        return self.Persons_repository.delete_Person(id)