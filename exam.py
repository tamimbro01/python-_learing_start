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
