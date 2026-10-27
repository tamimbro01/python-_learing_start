user_num = int(input("Enter a number "))

def number_pogisition_chack(user_num):
    if user_num > 0:
        print("Number is Positive")
    elif user_num < 0:
        print("Number is Negative")
    else: 
        print("Number is Zero")

number_pogisition_chack(user_num)