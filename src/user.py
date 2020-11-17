class User:
    __id = 0
    __username = ""
    __password = ""

    def __init__(self, id, *args, **kwargs):
        super().__init__()
        self.__id = id
        self.__username = kwargs.get('username')
        self.__password = kwargs.get('password')

    def get_id(self):
        return self.__id

    def login(self, username, password):
        if self.__username == username and self.__password == password:
            return True
        else:
            return False

    @staticmethod
    def register(new_username, new_password):
        return User(1, username=new_username, password=new_password)