class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee name {self.name}")

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department(self):
        print(f"department {self.department_name}")
        self.employee.show()

emp1 = Employee("Farhan")

dep1 = Department("IT", emp1)

dep1.show_department()

