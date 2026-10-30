#  1 question
# user_num = int(input("Enter a number "))
# def number_pogisition_chack(user_num):
#     if user_num > 0:
#         print("Number is Positive")
#     elif user_num < 0:
#         print("Number is Negative")
#     else:
#         print("Number is Zero")
# number_pogisition_chack(user_num)


#  2 question


# number = int(input("Enter a number chack even and odd  "))
# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is Even")
#     else:
#         print(f"{number} is Odd")
# for i in range(1, 11):
#     check_even_odd(i)


# Question 4
# Count Even and Odd Numbers
# even_count = 0
# odd_count = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(f"{i} is Even")
#         even_count += 1
#     else:
#         print(f"{i} is Odd")
#         odd_count += 1
# print("Total Even numbers:", even_count)
# print("Total Odd numbers:", odd_count)


# Question 5
# Number Guessing Game


# secret_number = 7
# guess_number = int(input("Enter the guess the number 1 to 10 :- "))
# def check_guess(guess_number, secret_number):
#         if guess_number == secret_number:
#             print("Correct Guess!")
#         elif guess_number < secret_number:
#             print( "Too Low!")
#         else:
#             print("Too High!")
# check_guess(guess_number, secret_number)


# Question 6
# Number Guessing Game — Retry Version

# secret_number = 7
# def check_retry(secret_number):
#     while True:
#         guess_user = int(input("Enter a number 1 to 11 :- "))
#         if guess_user == secret_number:
#             print('Correct Guess!')
#             break
#         elif guess_user < secret_number:
#             print('Too Low!')
#         else:
#             print('Too High!')
# check_retry(secret_number)


# Challenge 7
# Student Result Management System

# students = []
# student1 = {"name": "Tamim", "bangla": 85, "english": 78, "math": 92}
# student2 = {"name": "ìqbal", "bangla": 35, "english": 28, "math": 22}
# student3 = {"name": "Rakib", "bangla": 45, "english": 88, "math": 62}
# students.append(student1)
# students.append(student2)
# students.append(student3)
# def add_student(name, bangla, english, math):
#     if not name.strip():
#         print("Error : Name can't be empty")
#         return
#     marks = [bangla, english, math]
#     if any(
#         not isinstance(mark, int) or isinstance(mark, bool) or mark < 0 or mark > 100
#         for mark in marks
#     ):
#         print("Error: Marks must be integers from 0 to 100!")
#         return
#     student = {"name": name, "bangla": bangla, "english": english, "math": math}
#     students.append(student)
#     print(f"Student {name} added successfully")
# def calculate_result(student):
#     total = student["bangla"] + student["english"] + student["math"]
#     average = total / 3
#     if average >= 80:
#         grade = "A+"
#     elif average >= 70:
#         grade = "A"
#     elif average >= 60:
#         grade = "B"
#     elif average >= 50:
#         grade = "C"
#     elif average >= 40:
#         grade = "D"
#     else:
#         grade = "F"
#     return total, average, grade
# def show_results():
#     for student in students:
#         total, average, grade = calculate_result(student)
#         print(f"\nName: {student['name']}")
#         print(f"Total: {total}/300")
#         print(f"Average: {average:.2f}")
#         print(f"Grade: {grade}")
# def find_top_student():
#     if not students:
#         print("No students found!")
#         return
#     top_student = max(students, key=lambda student: calculate_result(student)[1])
#     total, average, grade = calculate_result(top_student)
#     print(f"\nTop Student: {top_student['name']}")
#     print(f"Average: {average:.2f}")
#     print(f"Grade: {grade}")
# def rank_students():
#     ranked_students = sorted(
#         students, key=lambda student: calculate_result(student)[1], reverse=True
#     )
#     print("\n--- Student Rankings ---")
#     for rank, student in enumerate(ranked_students, start=1):
#         total, average, grade = calculate_result(student)
#     print(f"{rank}. {student['name']} | " f"Average: {average:.2f} | Grade: {grade}")
# show_results()
# find_top_student()
# rank_students()
# add_student("Sakib", 75, 82, 90)
# show_results()


# Challenge 8
#  Inventory Stock Management

# products = [
#     {"name": "Keyboard", "price": 1200, "stock": 5},
#     {"name": "Mouse", "price": 500, "stock": 10},
#     {"name": "Monitor", "price": 12000, "stock": 3},
# ]
# def show_products():
#     for product in products:
#         print(f"Name {product['name']}")
#         print(f"Price {product['price']}")
#         print(f"Stock {product['stock']}")
#         print("--------------------")
# def sell_product(product_name, quantity):
#     for product in products:
#         if product["name"] == product_name:
#             if product["stock"] >= quantity:
#                 product["stock"] -= quantity
#                 print("Product Sold Successfully")
#                 print("Remaining stock:", product["stock"])
#             else:
#                 print("Out of Stock")
#                 return
# def calculate_inventory_value():
#     total = 0
#     for product in products:
#         total += product['price'] * product['stock']
#     print(f'Total Inventory Value: {total}')
# print("\nSelling Mouse...")
# sell_product("Mouse", 5)
# print("\nUpdated products:")
# show_products()
# calculate_inventory_value()


# Challenge 9
# Bus Ticket Booking System 🚌


# buses = [
#     {"bus_name": "Green Line", "destination": "Dhaka", "ticket_price": 800, "seats": 5},
#     {
#         "bus_name": "Hanif Enterprise",
#         "destination": "Chittagong",
#         "ticket_price": 600,
#         "seats": 3,
#     },
#     {"bus_name": "Shyamoli", "destination": "Sylhet", "ticket_price": 700, "seats": 4},
# ]
# def show_buses():
#     for bus in buses:
#         print(f"Bus Name: {bus['bus_name']}")
#         print(f"Destination: {bus['destination']}")
#         print(f"Ticket Price: {bus['ticket_price']}")
#         print(f"Available Seats: {bus['seats']}")
#         print("--------------------")
# def book_ticket(bus_name, quantity):
#     for bus in buses:
#         if bus["bus_name"] == bus_name:
#             if quantity <= 0:
#                 print("Invalid ticket quantity!")
#             elif bus["seats"] >= quantity:
#                 bus["seats"] -= quantity
#                 print("Ticket Booked Success")
#                 print(f"Bus Tickets avible {bus['seats']}")
#             else:
#                 print(f"Not enough seats!")
#                 return
#                 print("Bus not found")
# def calculate_ticket_cost(bus_name, quantity):
#     for bus in buses:
#         if bus["bus_name"] == bus_name:
#             if quantity <= 0:
#                 print("Invalid ticket quantity!")
#             else:
#                 total_ticket = bus["ticket_price"] * quantity
#     print("Total Ticket Cost :-", total_ticket)
#     return
# print("Bus not found!")
# print("\nBooking Tickets...")
# book_ticket("Green Line", 2)
# print("\nCalculating Ticket Cost...")
# calculate_ticket_cost("Green Line", 2)
# print("\nTesting Insufficient Seats...")
# book_ticket("Green Line", 10)
# print("\nTesting Unknown Bus...")
# book_ticket("Unknown Bus", 1)


# Challenge 10
# Car Rental Management System


# cars = [
#     {"name": "Toyota Corolla", "price_per_day": 2500, "available": True},
#     {"name": "Honda Civic", "price_per_day": 3500, "available": True},
#     {"name": "Toyota Noah", "price_per_day": 4500, "available": False},
# ]
# def show_cars():
#     for car in cars:
#         print(f"Name: {car['name']}")
#         print(f"Price Per Day: {car['price_per_day']}")
#         print(f"Available: {car['available']}")
#         print("--------------------")
# def rent_car(car_name, days):
#     for car in cars:
#         if car["name"] == car_name:
#             if car["available"] == True:
#                 car["available"] = False
#                 print("Car Rented Successfully")
#             else:
#                 print("Car is not available!")
#     else:
#         print("Car not found!")
# def calculate_rent(car_name, days):
#     if days < 1:
#         print("Invalide number of the days")
#         return
#         for car in cars:
#             if car["name"] == car_name:
#                 if car["available"] == True:
#                     car["available"] = False
#                     print("Car Rented Successfull")
#                     print("Rental Days: ", days)
#                 else:
#                     print("Car is not availabel")
#                 return
#         print("Car not foun")
# show_cars()
# print("\nRenting Car...")
# rent_car("Toyota Corolla", 1)
# print("\nCalculating Rent...")
# calculate_rent("Toyota Corolla", 3)
# print("\nTrying to Rent Unavailable Car...")
# rent_car("Toyota Noah", 2)
# print("\nTrying Unknown Car...")
# rent_car("BMW", 2)


# Challenge 11

# Restaurant Order Management System


# menus = [
#     {"name": "Burger", "price": 250, "available": True},
#     {"name": "Pizza", "price": 500, "available": True},
#     {"name": "Fries", "price": 150, "available": False},
#     {"name": "Sandwich", "price": 200, "available": True},
# ]
# def show_menu():
#     for menu in menus:
#         print(f"Name: {menu['name']}")
#         print(f"Price: {menu['price']}")
#         print(f"Available: {menu['available']}")
#         print("---------------------------")
# def place_order(food_name, quantity):
#     if quantity < 1:
#         print("Minimum order 1")
#         return
#     for menu in menus:
#         if menu["name"] == food_name:
#             if menu["available"] == True:
#                 print("Order created successfully!")
#             else:
#                 print("Food is not available!")
#             return
#     print("Food is not found!")
# def calculate_bill(food_name, quantity):
#     if quantity < 1:
#         print("Invalid quantity!")
#         return
#     for menu in menus:
#         if menu["name"] == food_name:
#             total_bill = menu["price"] * quantity
#             if total_bill >= 1000:
#                 discount_amount = total_bill * 10 / 100
#             elif total_bill >= 500:
#                 discount_amount = total_bill * 5 / 100
#             else:
#                 discount_amount = 0
#             final_price = total_bill - discount_amount
#             print("Total Bill:", total_bill)
#             print("Discount:", discount_amount)
#             print("Final Price:", final_price)
#             return
#     print("Food is not found!")
# show_menu()
# print("\nPlacing Order...")
# place_order("Burger", 3)
# print("\nCalculating Bill...")
# calculate_bill("Burger", 3)
# print("\nOrdering Unavailable Food...")
# place_order("Fries", 2)
# print("\nOrdering Unknown Food...")
# place_order("Pasta", 1)


# Challenge 12
# ATM Banking System

# accounts = [
#     {"name": "Tamim", "pin": "1234", "balance": 10000},
#     {"name": "Rahim", "pin": "5678", "balance": 5000},
#     {"name": "Karim", "pin": "9012", "balance": 20000},
# ]
# def login():
#     name = input(" Enter Your Account Name: ")
#     pin = input(" Enter Your PIN : ")
#     for acount in accounts:
#         if acount["name"] == name and acount["pin"] == pin:
#             print("login successful")
#             return acount
#     print("Invalid name or PIN!")
#     return None
# def check_balance(acount):
#     print("Current Balance: ", acount["balance"], "BDT")
# def deposit_money(acount):
#     amount = int(input("Enter deposit amount :"))
#     if amount > 0:
#         acount["balance"] += amount
#         print("Deposit successful")
#         print("New Balance: ", acount["balance"], "BDT")
#     else:
#         print("Invalid Amount")
# def withdraw_money(acount):
#     amount = int(input("Enter withdrawal amount: "))
#     if amount <= 0:
#         print("Invalid amount")
#     elif amount > acount["balance"]:
#         print("Insufficient balance!")
#     else:
#         acount["balance"] -= amount
#         print("Withdraw successful !")
#         print("Remaing Balance: ", acount["balance"], "BDT")
# def atm_menu(acount):
#     while True:
#         print("\n===== ATM MENU =====")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")
#         choice = input("Select an option : ")
#         if choice == "1":
#             check_balance(acount)
#         elif choice == "2":
#             deposit_money(acount)
#         elif choice == "3":
#             withdraw_money(acount)
#         elif choice == "4":
#             print("Thank you for useing our ATM !")
#             break
#         else:
#             print("INvalid Option !")
# user_account = login()
# if user_account is not None:
#     atm_menu(user_account)


# Challenge 13

# Hospital Appointment Management System


# doctors = [
#     {
#         "name": "Dr. Rahim",
#         "specialty": "Medicine",
#         "fee": 800,
#         "available": True
#     },
#     {
#         "name": "Dr. Karim",
#         "specialty": "Cardiology",
#         "fee": 1200,
#         "available": True
#     },
#     {
#         "name": "Dr. Hasan",
#         "specialty": "Medicine",
#         "fee": 600,
#         "available": False
#     }
# ]
# appointments = []
# def show_doctors():
#     for doctor in doctors:
#         if doctor['available'] == True:
#             print(f'Doctor Name: ', doctor['name'] )
#             print(f'specialty: ', doctor['specialty'] )
#             print(f'fee : ', doctor['fee'] )
#             print(f'available: ', doctor['available'] )
#             print('---------------------------')
# def book_appointment():
#     patient_name = input("Enter a Patient Name :- ")
#     doctor_name = input('Enter a  Doctor Name :- ')
#     found = False
#     for doctor in doctors:
#         if doctor['name'].lower() == doctor_name.lower():
#             found = True
#             if doctor['available'] == False:
#                 print('Doctor is not available!')
#             else:
#                 appointment ={
#                     "patient_name": patient_name,
#                     "doctor_name": doctor['name'],
#                     "fee": doctor['fee']
#                 }
#                 appointments.append(appointment)
#                 print(f"Appointment booked with {doctor['name']}")
#                 print(f"Patient Name: {patient_name}")
#                 print(f"Doctor Fee: {doctor['fee']}")
#                 break
#     if found == False:
#         print('Doctor not found!')
# def view_appointments():
#     if len(appointments) == 0:
#         print("No appointments found!")
#     else:
#         for appointment in appointments:
#             print("Patient:", appointment["patient_name"])
#             print("Doctor:", appointment["doctor_name"])
#             print("Fee:", appointment["fee"])
#             print("--------------------")
# view_appointments()
# def main_menu():
#     while True:
#         print("\n===== HOSPITAL MENU =====")
#         print("1. Book Appointment")
#         print("2. Show Available Doctors")
#         print("3. View Appointments")
#         print("4. Exit")
#         choice = input("choice the options")
#         if choice == "1":
#             book_appointment()
#         elif choice == "2":
#             show_doctors()
#         elif choice == "3":
#             view_appointments()
#         elif choice == "4":
#             print("Thank you!")
#             break
#         else:
#             print("Invalid option!")
# main_menu()
# # user_booking =  book_appointment()
# # if user_booking is not None:
# #     main_menu(user_booking)


#  Problem 14 — Student Performance Analyzer

# students = {"Rahim": 85, "Karim": 67, "Hasan": 42, "Nabil": 28}
# for name, marks in students.items():
#     if marks >= 33:
#         result = "Pass"
#     else:
#         result = "Faild"
#     print(f'{name} - {marks} - {result}')
