class Employ:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

obj_emp = Employ("Farhan", 10000, 123456)
print("Name: ", obj_emp.name)
print("salary: ", obj_emp._salary)
print("ssn: ", obj_emp._Employ__ssn)