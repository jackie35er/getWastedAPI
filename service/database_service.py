from persistance.meldung_repository import MeldungRepository


class DatabaseService:

    def __init__(self, link):
        self.__repository = MeldungRepository(link)

    def get_all(self):
        return self.__repository.get_all()
