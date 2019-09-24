from repositories.MoviesRepository import MoviesRepository

class MoviesService(object):
    def __init__(self):
        self.Movies_repository = MoviesRepository()

    def add_Movie(self, name):
        return self.Movies_repository.add_Movie(name)

    def get_all_Movies(self, page, pagesize, name):
        print("...service....name: " +name)
        return self.Movies_repository.get_all_Movies(page, pagesize, name)

    def get_Movie_by_id(self, id):
        return self.Movies_repository.get_Movie_by_id(id)

    def update_Movie(self, id, name):
        return self.Movies_repository.update_Movie(id, name)

    def delete_Movie(self, id):
        return self.Movies_repository.delete_Movie(id)