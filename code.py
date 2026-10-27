# fast_name = "Bro"

# age = 19
# age = 16 

# cgp = 1.1223

# do_work = True
# not_work = False


# name = input("Enter your name ")

# print('Hello' + name)

# print("My name is " + fast_name)
# print("My age is " + str(age))  
# print(type(age))         # output : int
# print(type(cgp))         # output : float
# print(type(do_work))     # output : bool
# print(type(not_work))    # output : bool


# input fron user 

# age = input('enter yyour agge ')
# age = float(age)
# print(age +1)  





# Type Conversion  & Type Casting  

# print(1 + 1.5)              #implicit 
# print(1 + int(2.999))       # explicit






# sum program 


# a = int(input('Enter a : '))
# b = int(input('Enter b : '))
# sum = a / b
# print('sum : ' , sum)





# name = "Tony Stark"
# grade = "A"

# print(name.upper())     # TONY STARK
# print(name.lower())     # tony stark
# print(name.find('a'))   # 3 index return
# print(name.replace('a' , 'A'))   # Tony StArk  


# print('S' in name)       # True
# print('f' in name)       # False 








# arithmetic oparitions
 
# print(5 + 2)      # 7
# print(5 - 2)      # 3
# print(5 * 2)      # 10
# print(5 / 2)      # 2.5
# print(5 % 2)      # 1  modulus operator  %  => remainder
# print(5 // 3)     # 1  floor division 
# print(2 ** 3)     # 8    


# assiment oparators

# x = 1 
# x += 2
# print(x)  # x = x + 2
# x -= 2
# print(x)   # x = x - 2
# x *= 2
# print(x)   # x = x * 2
# x /= 2
# print(x)   # x = x / 2
# x %= 2
# print(x)   # x = x % 2
# x **= 2
# print(x)   # x = x ** 2






# Operator Precedence

# result = 2 + 3 * 4
# result =( 2 + 3) * 4
# print(result)


# Comparision Operator

# print(2 > 2)
# print(2 > 3)
# print(3<3) 
# print(3< 4)





# Logical Operators

# stat1 = 3 > 5
# stat2 = 3 == 1
# print(stat1 and stat2)
# print(stat1 or stat2)
# print(not stat2) 



#  Conditional Statements



#indentation 

# age = int(input('Enter your age : ')) 
# if age >= 18:
#     print("Adult")
# elif age >= 15:
#     print('teenager')
# else :            
#     print('Not a adult') 


# marsk = int(input("enter your mark "));
# if marsk >= 80:
#     print("A+")
# elif marsk >= 70:
#     print("A")
# elif marsk >= 60:
#     print("A-")
# elif marsk >= 50:
#     print("B+")
# elif marsk >= 40:
#     print("B")
# elif marsk >= 30:
#     print("C+")
# else:
#     print("F")














# calculator 

# a = int(input('Input Fast Number '))
# oparater = input('Enter oparater (+ , - , * , /, ** , // , %)')
# b = int(input('Input second Number '))
# if oparater == '+':
#     print(a + b)
# elif oparater == '-':
#     print(a -b)
# elif oparater == '*':
#     print(a * b)
# elif oparater == '/':
#     print(a / b)
# elif oparater == '**':
#     print(a ** b)
# elif oparater == '//':
#     print(a // b)
# elif oparater == '%':
#    print(a  % b)
# else:
#     print('Invalid oparater')

 


#  part 4

# Range 

# number = range(20)
# print(number)  


# While Loop
  
# counter = 1
# while counter <=10:
#     print('*' * counter )
#     counter = counter + 1
# print("End of Tamim") 




#  For Loop

# for i in range(2): 
#     print(i)


# 1 to 10 => even

# num = int(input("Enter number chack ever and odd"))
# numBr = int(input("set a stop number or brack "))
# for i in range (num):
#     if i == numBr:
#         break
#     if i % 2 == 0:
#         print('Event Numebr' , i)
#         continue 
#     else:
#         print('Odd Numebr' , i)



# part 5

# List & slicing => metuble 

# marks = [ 12, 32, 43, 65, 67, 88, 87,98 , 64]
# print(len(marks)) 
# print(marks[-1])
# print(marks[0:4]) 
# print(marks[-4:-1]) 
# print(marks[-4:]) 
# for score in marks:
#     print(score)
# marks.append(3999)
# marks.insert(2, 4434)
# print(marks)




# Tuple => immutible

# marks = (3,4,5,6,67,4,3,33,4)
# print(marks)
# print(marks.count(4))



# Set => unique item collection

# marks = {34, 56,44,444,44,4,44,44,55}
# print(len(marks))
# for score in marks:
#     print(score)

 
# Dictionary => key-value => mutible


# student = {'name':'Tamim','age':22, 'cgpa': 3.5 , 'math': 20}
# for key in student:
#     print(key, student[key]) 
# student['name'] = "Iqbal"
# print(student) 
# print(student['math'])



# Funcation 


# a = int(input('Enter a : ')) 
# b = int(input('Enter b : '))
# def sum(a , b):                 # funcation defining
#     print(a + b) 
# sum( a, b)                      #Funcation Calling

# price = int(input('Enter price of product : ')) 
# persent = int(input('Enter persent of gst : ')) 
#             # parameties
# def cal_gst(price , persent):
#     new_price = price +( price * persent / 100)
#     print(new_price) 
#          # argument   
# cal_gst(price, persent)






# Inbuilt Funcation

# print("Hello")
# print(len([1,2,345,66,77,32233,22233,443334]))

# Module Funcation

# from math import sqrt , log2
# print(log2(16))             # 4 because 2^4 = 16
# print(sqrt(16))             # 4 because 4^2 = 16 

# import random

# print(random.random())
# print(random.randint(100, 200)) 