# user.py
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def login(self):
        pass
