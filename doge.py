import sys
import random


print("You have a new pet dog!")
name = input("Name the dog: ")
print("Your dog's name is " +name+ ".")
runprogram = True
counter = 0
counter2 = 0
clean = False
found = False
print("You can give your dog a treat, take it on a walk, play with it, or give it a bath.")
print("When you're ready to quit, just type end program")
while runprogram == True:
  do = input("What will you do now? ")
  if do == "end program":
    sys.exit("See you next time!")
  elif do == "shoot it":
    sys.exit("What is wrong with you?")
  elif do == "treat":
    if counter >= 3:
      print(name+ " is full!")
    elif counter == 0:
      print("You fed "+name+ " a treat!")
      counter = counter+1
      counter2 = counter2 - 1
    else:
      print("You fed "+name+ " another treat!")
      counter = counter+1
      counter2 = counter2 - 1
  elif do == "walk":
    if counter2 >= 2:
      print(name + " is too tired to walk")
    else:
      print("You took "+name+ " for a walk!")
      counter = counter - 1
      counter2 = counter2 + 1
      clean = False
  elif do == "play":
    print("Let's play a short game!")
    number = random.randint(1,100)
    while not(found):
      guess = int(input("Guess a number between 1 and 100: "))
      if guess == number:
       print(name+ " caught the ball!")
       counter = counter - 1
       clean = False
       found = True
      elif guess < number:
       print("Your guess is too low.")
      else:
        print("Your guess is too high.")
  elif do == "bath":
    if clean == True:
      print(name+ " doesn't need a bath!")
    else:
      print("You gave "+name+ " a bath!")
      clean = True