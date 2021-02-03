class Guest:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
class MoreInf(Guest):
    def __init__(self, firstname, lastname, city, status):
        super().__init__(firstname, lastname)
        self.city = city
        self.status = status
    def getGuest(self):
        print("{}, {}, г. {}, статус {}".format(self.firstname, self.lastname, self.city, self.status))

guest1 = MoreInf("Иван", "Иванов", "Москва", "наставник")
print(guest1.getGuest())

