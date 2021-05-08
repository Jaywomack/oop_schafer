# python Object Oriented Programming


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jay', 'Womack', 150000)

print(emp_2.first)
print(emp_1.pay)
print(emp_1.fullname())
print(emp_2.fullname())

