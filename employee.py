from user import User

class Employee(User):
    def __init__(self, username, password, role):
        super().__init__(username, password)
        self.role = role

    def register(self):
        # Реализация регистрации для сотрудника
        pass

    def login(self):
        # Реализация входа для сотрудника
        pass