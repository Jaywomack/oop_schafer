# python Object Oriented Programming

# regular methods take the instance as the first argument

# class methods take the class as the first argument
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay, phone):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.phone = phone

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Corey', 'Schafer', 50000, '509')
emp_2 = Employee('Jay', 'Womack', 150000, '208')

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
