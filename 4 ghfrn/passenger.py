from user import User
import sqlite3

class Passenger(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = "Passenger"
        self.tickets = []

    def get_role(self):
        return self.role

    def authorize(self):
        # Реализация авторизации для пассажира
        print(f"Пассажир {self.username} авторизован.")

    def register(self):
        # Реализация регистрации для пассажира
        print(f"Пассажир {self.username} успешно зарегистрирован.")

    def book_ticket(self, flight):
        # Добавление билета
        if isinstance(flight, Flight):
            conn = sqlite3.connect('airport_system.db')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO tickets (passenger_id, flight_id) VALUES (?, ?)',
                           (self.id, flight.id))

            conn.commit()
            conn.close()

            self.tickets.append(flight)
            print(f"Билет на рейс {flight.flight_number} успешно забронирован.")
        else:
            print("Ошибка: Неверный рейс.")
