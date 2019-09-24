from repositories.fcmoviesRepository import fcmoviesRepository

class fcmoviesService(object):
    def __init__(self):
        self.fcmovies_repository = fcmoviesRepository()

    def add_Fcmovies(self, name):
        return self.fcmovies_repository.add_Fcmovies(name)

    def get_all_fcmovies(self, page, pagesize, name):
        print("...service....name: " +name)
        return self.fcmovies_repository.get_all_fcmovies(page, pagesize, name)

    def get_Fcmovies_by_id(self, id):
        return self.fcmovies_repository.get_Fcmovies_by_id(id)

    def update_Fcmovies(self, id, name):
        return self.fcmovies_repository.update_Fcmovies(id, name)

    def delete_Fcmovies(self, id):
        return self.fcmovies_repository.delete_Fcmovies(id)