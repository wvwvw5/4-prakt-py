from datetime import datetime
from user import User
from passenger import Passenger
from employee import Employee
from flight import Flight

# Пример использования
passenger1 = Passenger("passenger1", "pass123")
employee1 = Employee("employee1", "emp456")

flight1 = Flight("ABC123", "CityA", "CityB", str(datetime.now()))
flight2 = Flight("XYZ789", "CityC", "CityD", str(datetime.now()))

employee1.add_flight(flight1)
employee1.add_flight(flight2)

passenger1.book_ticket(flight1)

# Просмотр билетов пассажира
print("Билеты пассажира:")
for ticket in passenger1.tickets:
    print(f"{ticket.flight_number} - {ticket.departure} to {ticket.destination}")
