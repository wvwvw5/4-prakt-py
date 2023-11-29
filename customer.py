from user import User

class Customer(User):
    def __init__(self, username, password, email):
        super().__init__(username, password)
        self.email = email

    def register(self):
        # Реализация регистрации для клиента
        pass

    def login(self):
        # Реализация входа для клиента
        pass