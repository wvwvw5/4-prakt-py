import sqlite3
from datetime import datetime

class Flight:
    def __init__(self, flight_number, departure, destination, departure_time):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.departure_time = departure_time
