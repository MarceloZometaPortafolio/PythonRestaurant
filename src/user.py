class User:
    __id = 0

    def __init__(self, id):
        super().__init__()
        self.__id = id

    def get_id(self):
        return self.__id

    