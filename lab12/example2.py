class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def set_name(self, name):
        self.name = name
    def set_salary(self, salary):
        self.salary = salary
    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Company:
    def __init__(self):
        self.employee_list = []
    def get_employee_list(self):
        return self.employee_list
    def set_employee_list(self, employee_list):
        self.employee_list = employee_list
    def add_employee(self, new_employee):
        if isinstance(new_employee, Employee):
            self.employee_list.append(new_employee)
    def calc_avg_salary(self):
        total_salary = 0
        for employee in self.employee_list:
            total_salary += employee.salary
        avg_salary = total_salary / len(self.employee_list)
        return avg_salary
    def display_all_info(self):
        for employee in self.employee_list:
            employee.display_info()

company = Company()
e1 = Employee("sude", 500)
e2 = Employee("ebru", 3900)
e3 = Employee("sude", 2500)
company.add_employee(e1)
company.add_employee(e2)
company.add_employee(e3)
company.display_all_info()