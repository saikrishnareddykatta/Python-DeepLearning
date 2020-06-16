class Employee:
    no_of_employees = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.no_of_employees = Employee.no_of_employees + 1
        Employee.total_salary = Employee.total_salary + salary

    def average_salary(self):
        avg_salary = self.total_salary / self.no_of_employees
        print(avg_salary)

    def get_name(self):
        return self.name


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)


# Instances created using Employee or base class
e1 = Employee("Sai", "Katta", 10000, "CS")

e2 = Employee("Krishna", "Reddy", 20000, "CS")

# Instances created using FullTimeEmployee or derived class
e3 = FullTimeEmployee("Ravi", "Kummara", 30000, "CS")

e4 = FullTimeEmployee("Abhinay", "Yadav", 40000, "CS")

print("No of Employees:")
print(Employee.no_of_employees)
print("Total Salary of the Employees")
print(Employee.total_salary)
print("Name of the Employees: ")
# Instances are created using super class, derived class and their member functions are being called
print(e1.get_name())
print(e2.get_name())
print(e3.get_name())
print(e4.get_name())
print("Average Salary of the Employees:")
e4.average_salary()
