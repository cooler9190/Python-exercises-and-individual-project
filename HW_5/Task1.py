# 1.Employee Management System Using OOP
# Task: Define classes for managing employees, including classes for Employee, Manager, Engineer, etc.
# Implement methods for promotions, demotions, and salary adjustments.
# Example Input: employee.promote()
# Example Output: Promotion successful. New title: Manager

class Employee:
    #salary_multiplier =
    def __init__(self, name, salary, title="Employee"):
        self.name = name
        self.salary = salary
        self.title = title

    def promote(self):
        pass

    def demote(self):
        pass

    def salary_adjustment(self, new_salary):
        self.salary += new_salary


class Manager(Employee):
    def __init__(self, name, salary, title="Manager"):
        super().__init__(name, salary, title)

    def promote(self):
        self.title = "Senior Manager"
        self.salary_adjustment(5000)
        print(self.name + "'s new title: " + self.title + " and new salary: " + str(self.salary))

    def demote(self):
        self.title = "Employee"
        self.salary_adjustment(-5000)
        print(self.name + "'s new title: " + self.title + " and new salary: " + str(self.salary))


class Engineer(Employee):
    def __init__(self, name, salary, title="Engineer"):
        super().__init__(name, salary, title)

    def promote(self):
        self.title = "Senior Engineer"
        self.salary_adjustment(4000)
        print(self.name + "'s new title: " + self.title + " and new salary: " + str(self.salary))

    def demote(self):
        self.title = "Junior Engineer"
        self.salary_adjustment(-4000)
        print(self.name + "'s new title: " + self.title + " and new salary: " + str(self.salary))


employee1 = Manager("Winston Smith", 10000)

employee2 = Engineer("Sarah Wesker", 9000)

employee1.demote()

employee2.promote()
