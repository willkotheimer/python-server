class Employee:
    def __init__(self, name, position='sales', hourly_rate=20, shift=1):
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.shift = shift

person_one = Employee('Bob')
person_two = Employee('Cheryl', 'maintenance', shift=2, hourly_rate=25)

print(person_one.__dict__);
print(person_two.__dict__);