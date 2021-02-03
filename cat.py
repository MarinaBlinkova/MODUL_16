class Cat:
    def __init__(self, name, gender, age):
         self.name = name
         self.gender = gender
         self.age = age

    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getAge(self):
        return self.age
    def getList(self):
        print('Кличка - {}'.format(self.name))
        print('Пол - {}'.format(self.gender))
        print('Возраст - {}'.format(self.age))