# -*- coding: utf-8 -*-
"""Task_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-rPk5aVG6e9aPCNleCxdJ293H0OEGrC

### TASK TWO: OPERATORS AND DECISION-MAKING STATEMENT

#### **1 to 8 already done **
9. Read the two parts of the question below: 
 Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question of whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
"""

t0209_luckyNum = 3
t0209_guessNum = input ("Guess the lucky number :")
i=1
while True:
  if t0209_guessNum == str(t0209_luckyNum):
    print ("Good guess")
    break
  elif t0209_guessNum !=str(t0209_luckyNum):
    t0209_tryAgain = input("wrong guess, try again ")
    if t0209_tryAgain == str(t0209_luckyNum):
      print ("Good guess")
      break
    elif t0209_tryAgain in ['no', 'No', 'Nope', 'nope']:
      print ("Thanks for playing...")
      break
  # i+=1
  # if i>=5:
  #   print ("You already tried for", i, "times, Game over")
  #   break

"""####10.  Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as  
```
counter=1
While counter <= 5:
  print(“Type in the”, counter, “number”
  counter=counter+1
```
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess, it stops and prints “Game over!”.
"""

t0210_luckyNum = 4
t0210_counter = 1
while t0210_counter <= 5:
  
  t0210_guessNum = input ("Guess the lucky number :")

  if t0210_guessNum == str(t0210_luckyNum):
    print ("Good guess!")
  elif t0210_guessNum !=str(t0210_luckyNum):
    print ("Try again!")
 
  if t0210_counter >= 5:
    print ("Game over")
  
  t0210_counter += 1

"""#### 11.  In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”."""

t0211_luckyNum = 4
t0211_counter = 1
while t0211_counter <= 5:

  t0211_guessNum = input ("Guess the lucky number :")
  if t0211_guessNum == str(t0211_luckyNum):
    print ("Good guess! \nbreak")
    break
  elif t0211_guessNum !=str(t0211_luckyNum):
    print ("Try again!")
 
  if t0211_counter >= 5:
    print ("“Sorry but that was not very successful")
  t0211_counter += 1