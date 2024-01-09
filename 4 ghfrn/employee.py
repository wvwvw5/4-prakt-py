import sqlite3
from flight import Flight  # Добавлен импорт класса Flight
from user import User

class Employee(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Employee"

    def get_role(self):
        return self.role

    def authorize(self):
        print(f"Сотрудник {self.username} авторизован.")

    def register(self):
        print(f"Сотрудник {self.username} успешно зарегистрирован.")

    def add_flight(self, flight):
        if isinstance(flight, Flight):
            conn = sqlite3.connect('airport_system.db')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO flights (flight_number, departure, destination, departure_time) VALUES (?, ?, ?, ?)',
                           (flight.flight_number, flight.departure, flight.destination, flight.departure_time))

            conn.commit()
            conn.close()

            print(f"Рейс {flight.flight_number} успешно добавлен.")
        else:
            print("Ошибка: Неверная информация о рейсе.")
