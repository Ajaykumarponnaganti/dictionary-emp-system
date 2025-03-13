# Solution

# Employee dictionary (Key: Employee ID, Value: Employee Details)
employees = {}

# Function to add a new employee
def add_employee():
    emp_id = input("Enter Employee ID : ")
    if emp_id in employees:
        print("Employee ID already exists!")
        return
    name = input("Enter Name: ")
    if not name.replace(" ", "").isalpha():
        print("Invalid name! Only alphabets allowed.")
        return
    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Age must be a positive number!")
            return
    except ValueError:
        print("Invalid age! Enter a number.")
        return

    dept = input("Enter Department: ")
    
    employees[emp_id] = {"name": name, "age": age, "department": dept}
    print("Employee added successfully!")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully!")
    else:
        print("Employee not found!")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee not found!")
        return

    name = input("Enter new Name: ")
    if name and not name.replace(" ", "").isalpha():
        print("Invalid name!")
        return
    
    age = input("Enter new Age: ")
    if age:
        try:
            age = int(age)
            if age <= 0:
                print("Invalid age!")
                return
        except ValueError:
            print("Invalid input!")
            return
    
    dept = input("Enter new Department: ")

    if name:
        employees[emp_id]["name"] = name
    if age:
        employees[emp_id]["age"] = age
    if dept:
        employees[emp_id]["department"] = dept

    print("Employee details updated successfully!")

def search_employee():
    query = input("Enter Employee ID or Name to search: ").lower()
    for emp_id, details in employees.items():
        if emp_id.lower() == query or details["name"].lower() == query:
            print(f"Found: {emp_id} - {details['name']} - {details['age']} - {details['department']}")
            return
    print("Employee not found!")

def view_employees():
    if not employees:
        print("No employees found!")
        return

    sorted_employees = sorted(employees.items(), key=lambda x: x[1]["name"])
    print("\nEmployee List:")
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details['name']} - {details['age']} - {details['department']}")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Remove Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        remove_employee()
    elif choice == "6":
        print("Thank you for using. Have a great day ahead! ")
        break
    else:
        print("Invalid choice! Please try again.")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Output :-
Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit
Enter your choice: 1
Enter Employee ID : E101
Enter Name: ajay
Enter Age: 22
Enter Department: employee
Employee added successfully!

Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit
Enter your choice: 2

Employee List:
E101: ajay - 22 - employee

Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit

Enter your choice: 3
Enter Employee ID or Name to search: E101
Found: E101 - ajay - 22 - employee


Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit

Enter your choice: 4
Enter Employee ID to update: E101
Enter new Name: Ajay
Enter new Age: 22
Enter new Department: employee
Employee details updated successfully!


Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit

Enter your choice: 1
Enter Employee ID : E101
Employee ID already exists!


Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit

Enter your choice: 1
Enter Employee ID : e101
Enter Name: ajay
Enter Age: 22
Enter Department: jk
Employee added successfully!


Employee Management System
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Remove Employee
6. Exit

Enter your choice: 6
Thank you for using. Have a great day ahead!
