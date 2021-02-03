class Client:
    def __init__(self, firstname, lastname, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def getClient(self):
        print("Клиент: {} {}, Баланс: {} руб.".format(self.firstname, self.lastname, self.balance))
client1 = Client("Екатерина", "Белова", "1020")
print(client1.getClient())
