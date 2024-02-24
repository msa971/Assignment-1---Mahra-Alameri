from enum import Enum


class Destination(Enum):
    Maldives = 1
    Paris = 2
    Italy = 3
    NewYork = 4
    Austrailia = 5


class Class(Enum):
    Economy = 1
    Business = 2
    First = 3


class Type(Enum):
    Window = 1
    Middle = 2
    Aisle = 3


class Size(Enum):
    small = 1
    medium = 2
    large = 3
    xlarge = 4


class Gender(Enum):
    female = 1
    male = 2


class Passenger:
    """Class to represent a Passenger"""

    # Constructor:
    def __init__(self, firstname, lastname, passportnum, gender, age):
        self.firstname = firstname
        self.lastname = lastname
        self.passportnum = passportnum
        self.gender = gender
        self.age = age

    # Setter getter functions:
    def setfirstname(self, firstname):
        self.firstname = firstname

    def getfirstname(self):
        return self.firstname

    def setlastname(self, lastname):
        self.lastname = lastname

    def getlastname(self):
        return self.lastname

    def setpassportnum(self, passportnum):
        self.passportnum = passportnum

    def getpassportnum(self):
        return self.passportnum

    def setgender(self, gender):
        self.gender = gender

    def getgender(self):
        return self.gender

    def setage(self, age):
        self.age = age

    def getage(self):
        return self.age


class Luggage:
    """Class to represent passenger Luggage"""

    # Constructor:
    def __init__(self, weight, count, luggage_destination, label_number, size):
        self.weight = weight
        self.count = count
        self.luggage_destination = luggage_destination
        self.label_number = label_number
        self.size = size

    # Setter getter functions:
    def setweight(self, weight):
        self.weight = weight

    def getweight(self):
        return self.weight

    def setcount(self, count):
        self.count = count

    def getcount(self):
        return self.count

    def setluggage_destination(self, luggage_destination):
        self.luggage_destination = luggage_destination

    def getluggage_destination(self):
        return self.luggage_destination

    def setlabel_number(self, label_number):
        self.label_number = label_number

    def getlabel_number(self):
        return label_number

    def setsize(self, size):
        self.size = size

    def getsize(self):
        return self.size


class Flight:
    """Class to represent a Flight"""

    # Constructor:
    def __init__(self, departure, departure_time, date, boardingtill, arrival, flight_destination, flight_number, gate,
                 terminal):
        self.departure = departure
        self.departure_time = departure_time
        self.date = date
        self.boardingtill = boardingtill
        self.arrival = arrival
        self.flight_destination = flight_destination
        self.flight_number = flight_number
        self.gate = gate
        self.terminal = terminal

    # Setter getter functions:
    def setdeparture(self, departure):
        self.departure = departure

    def getdeparture(self):
        return self.departure

    def setdeparture_time(self, departure_time):
        self.departure_time = departure_time

    def getdeparture_time(self):
        return self.departure_time

    def setdate(self, date):
        self.date = date

    def getdate(self):
        return self.date

    def setboardingtill(self, boardingtill):
        self.boardingtill = boardingtill

    def getboradingtill(self):
        return self.boardingtill

    def setarrival(self, arrival):
        self.arrival = arrival

    def getarrival(self):
        return self.arrival

    def setflight_destination(self, flight_destination):
        self.flight_destination = flight_destination

    def getflight_destination(self):
        return self.flight_destination

    def setflight_number(self, flight_number):
        self.flight_number = flight_number

    def getflight_number(self):
        return self.flight_number

    def setgate(self, gate):
        self.gate = gate

    def getgate(self):
        return self.gate

    def setterminal(self, terminal):
        self.terminal = terminal

    def getterminal(self):
        return terminal


class Seat:
    """Class to represent a Seat in the airplane"""

    # Constructor:
    def __init__(self, seat_type, seat_num, seat_class, seat_price, seat_availability):
        self.seat_type = seat_type
        self.seat_num = seat_num
        self.seat_class = seat_class
        self.seat_price = seat_price
        self.seat_availability = seat_availability

    # Setter getter functions:
    def setseat_type(self, seat_type):
        self.seat_type = seat_type

    def getseat_type(self):
        return self.seat_type

    def setseat_num(self, seat_num):
        self.seat_num = seat_num

    def getseat_num(self):
        return self.seat_num

    def setseat_class(self, seat_class):
        self.seat_class = seat_class

    def getseat_class(self):
        return self.seat_class

    def setseat_price(self, seat_price):
        self.seat_price = seat_price

    def getseat_price(self):
        return self.seat_price

    def setseat_availability(self, seat_availability):
        self.seat_availability = seat_availability

    def getseat_availability(self):
        return self.seat_availability


passenger1 = Passenger("James", "Smith", "BA876N7", Gender.male, "19")
passengerLuggage = Luggage(21.9, 1, Destination.NewYork, 213455, Size.medium)
passengerFlight = Flight("Chicago ORD", "11:40", "06 Dec 20", "11:20", "13:30", Destination.NewYork, "NA4321", "03", 2)
passengerSeat = Seat(Type.Window, "09-A", Class.First, 9999.99, "Available")

print("Passenger Boarding Pass information: ")
print("\nFirst name: ", passenger1.firstname)
print("Last name: ", passenger1.lastname)

print("Departure:", passengerFlight.departure)
print("Departure Time:", passengerFlight.departure_time)
print("Date: ", passengerFlight.date)
print("Boarding till: ", passengerFlight.boardingtill)
print("Arrival:", passengerFlight.arrival)
print("Flight Destination:", passengerFlight.flight_destination.name)
print("Flight Number:", passengerFlight.flight_number)
print("Gate:", passengerFlight.gate)
print("Terminal: ", passengerFlight.terminal)
print("Seat Number:", passengerSeat.seat_num)
print("Please be at the gate at boarding time!")

print("\nExtra Information: ")
print("Passport Number: ", passenger1.passportnum)
print("Gender: ", passenger1.gender)
print("Age: ", passenger1.age)
print("\nLuggage Information:")
print("Weight: ", passengerLuggage.weight)
print("Count:", passengerLuggage.count)
print("Destination:", passengerLuggage.luggage_destination.name)
print("Label Number:", passengerLuggage.label_number)
print("Size:", passengerLuggage.size.name)

print("\nSeat Information:")
print("Type:", passengerSeat.seat_type.name)
print("Seat Number:", passengerSeat.seat_num)
print("Class:", passengerSeat.seat_class.name)
print("Price:", passengerSeat.seat_price)
print("Availability:", passengerSeat.seat_availability)