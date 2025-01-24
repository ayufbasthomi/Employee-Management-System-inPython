import os

FILENAME = "employees.txt"

class Employee:
    def __init__(self, emp_id, name, phone, position, email):
        self.id = emp_id
        self.name = name
        self.phone = phone
        self.position = position
        self.email = email

    def __str__(self):
        return f"{self.id},{self.name},{self.phone},{self.position},{self.email}"

# Helper function to validate ID (3-digit numeric)
def is_valid_id(emp_id):
    return len(emp_id) == 3 and emp_id.isdigit()

# Helper function to validate phone number (XX-XXX-XXXX or XXX-XXXX-XXXX)
def is_valid_phone(phone):
    if len(phone) not in [11, 13]:  # Check length
        return False
    parts = phone.split("-")
    if len(parts) != 3:
        return False
    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False
    if len(parts[0]) not in [2, 3] or len(parts[1]) not in [3, 4] or len(parts[2]) != 4:
        return False
    return True

# Helper function to validate email format
def is_valid_email(email):
    if "@" not in email or "." not in email:
        return False
    local, domain = email.rsplit("@", 1)
    if "." not in domain or len(local) == 0 or len(domain.split(".")[-1]) < 2:
        return False
    return True

# Load employees from file
def load_employees():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        lines = file.readlines()
    employees = []
    for line in lines:
        emp_data = line.strip().split(",")
        if len(emp_data) == 5:
            employees.append(Employee(*emp_data))
    return employees

# Save employees to file
def save_employees(employees):
    with open(FILENAME, "w") as file:
        for emp in employees:
            file.write(str(emp) + "\n")

# Add a new employee
def add_employee():
    emp_id = input("Enter Employee ID (3-digit numeric): ")
    if not is_valid_id(emp_id):
        print("Invalid ID format! Must be 3 digits.")
        return

    employees = load_employees()
    if any(emp.id == emp_id for emp in employees):
        print("Employee ID must be unique!")
        return

    name = input("Enter Name: ")
    phone = input("Enter Phone Number (XX-XXX-XXXX or XXX-XXXX-XXXX): ")
    if not is_valid_phone(phone):
        print("Invalid phone number format!")
        return

    position = input("Enter Position: ")
    email = input("Enter Email Address: ")
    if not is_valid_email(email):
        print("Invalid email address format!")
        return

    employees.append(Employee(emp_id, name, phone, position, email))
    save_employees(employees)
    print("Employee added successfully!")

# List all employees
def list_employees():
    employees = load_employees()
    if not employees:
        print("No employees found.")
        return

    print("Employee List:")
    for emp in sorted(employees, key=lambda x: x.id):
        print(f"ID: {emp.id}, Name: {emp.name}, Phone: {emp.phone}")

# View detailed information of an employee
def view_employee():
    emp_id = input("Enter Employee ID: ")
    employees = load_employees()

    for emp in employees:
        if emp.id == emp_id:
            print(f"ID: {emp.id}\nName: {emp.name}\nPhone: {emp.phone}\nPosition: {emp.position}\nEmail: {emp.email}")
            return

    print("Employee not found!")

# Edit an employee's information
def edit_employee():
    emp_id = input("Enter Employee ID to edit: ")
    employees = load_employees()

    for emp in employees:
        if emp.id == emp_id:
            print(f"Editing Employee: {emp.name}")

            name = input("Enter New Name (leave blank to keep current): ")
            if name:
                emp.name = name

            phone = input("Enter New Phone (leave blank to keep current): ")
            if phone and is_valid_phone(phone):
                emp.phone = phone

            position = input("Enter New Position (leave blank to keep current): ")
            if position:
                emp.position = position

            email = input("Enter New Email (leave blank to keep current): ")
            if email and is_valid_email(email):
                emp.email = email

            save_employees(employees)
            print("Employee updated successfully!")
            return

    print("Employee not found!")

# Delete an employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    employees = load_employees()

    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            save_employees(employees)
            print("Employee deleted successfully!")
            return

    print("Employee not found!")

# Main menu
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. View Employee")
        print("4. Edit Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            view_employee()
        elif choice == "4":
            edit_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
