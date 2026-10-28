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