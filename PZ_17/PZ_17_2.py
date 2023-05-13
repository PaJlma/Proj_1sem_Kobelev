class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f"{self.name} работает...")

    def getSalary(self, money):
        print(f"{self.name} получает зарплату в размере {money} рублей!")

class Manager(Worker):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def manage(self):
        print(f"{self.name} управляет командой!")

class Engineer(Worker):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def design(self):
        print(f"{self.name} проектирует системы!")

worker = Worker('Anton', 17)
manager = Manager('Eugene', 18)
engineer = Engineer('Max', 17)

worker.work()
worker.getSalary(40000)

manager.work()
manager.getSalary(40000)
manager.manage()

engineer.work()
engineer.getSalary(40000)
engineer.design()