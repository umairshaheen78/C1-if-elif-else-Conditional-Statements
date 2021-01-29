'''
1/28/2021

Review: 

if/else conditonal statement

if (condtion):
 BODY STATEMENT1
else:
  BODY STATEMENT2

 Condition:
 a == b
 - Boolean Expression; True or False

 a == b
 1 >= 0
 a = 5

if/elif/else conditional statement
- used for decision-making operations with conditions

Formula:
if (Condition)
 Body statement

elif (Condition):
  Body statement

elif (Condition):
  Body statement

Condition:
An expression that evaluates to produce a result which is a Boolean value (Boolean expression) 

In a conditional statement,
1 x if header
infinite (∞) x elif header(s)
1 x (optional) else cause

1 x (Maximum) output/result
Minimum (None)

a = 2

if (a == 0):
  print ("Hi!")

  if (a == 2):
    print("Hello!")

elif (a != 2):
  print("Welcome!")

else:
  print ("bye")

a = 5000
num = int(input("Enter a number: "))

if (num > 0):
  print (" I see that your number is positive!")
elif (num == 0):
 print (" You entered 0!")
else:
  print ("Its negative!")

'''

# Ask the user for their age
# If they are younger than 13, tell them they can only watch PG/G movies
# If they are older than 13, but younger than 17, they can watch PG-13/PG/G movies
# If they are 17 and older, they can watch all the movies

age = int(input("What is your age?"))
print("Cool! That's nice to know!")
if (age < 13):
 print (" You can only watch PG and G movies!")
elif (age < 17):
 print ("You can watch PG-13/PG/G movies!")
elif (age > 17 ):
 print ("You can watch any movie!")


