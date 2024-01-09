from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def register(self):
        pass
