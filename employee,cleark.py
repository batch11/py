class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        
# Derived class Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        # Call the constructor of the parent class (Employee)
        super().__init__(name, employee_id, salary)
        self.department = department
    
    def display_info(self):
        # Call the base class display_info method
        super().display_info()
        print(f"Department: {self.department}")
    
    def manage_team(self):
        print(f"{self.name} is managing the {self.department} team.")
        
# Derived class Clerk inherits from Employee
class Clerk(Employee):
    def __init__(self, name, employee_id, salary, office_location):
        # Call the constructor of the parent class (Employee)
        super().__init__(name, employee_id, salary)
        self.office_location = office_location
    
    def display_info(self):
        # Call the base class display_info method
        super().display_info()
        print(f"Office Location: {self.office_location}")
    
    def assist_in_office(self):
        print(f"{self.name} is assisting in the office located at {self.office_location}.")
        
# Creating objects of Manager and Clerk classes
manager = Manager("Shruti", 101, 75000, "HR")
clerk = Clerk("Shree", 102, 35000, "Block A")

# Displaying information and demonstrating functionality of both classes
print("Manager Information:")
manager.display_info()
manager.manage_team()

print("\nClerk Information:")
clerk.display_info()
clerk.assist_in_office()
