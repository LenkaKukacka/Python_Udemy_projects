import time #jak importovat modul
print ("Hello!")
time.sleep(1) #modul.fce()
name = input("What is your name?" ) #ask user, get variable
print("Nice to meet you, " + name + "!") #vypiš, vše, co chceš vidět/vypsat, musíš dát print. Prázdny řádek print()
time.sleep(1)
sport = input("What is your favourite sport? ")
print ("So, your favourite sport is " + sport + ".")
print()
#Aktivita:
#import time
print("First Activity:")
print("Hello.")
time.sleep(1)
name = input("What is your name?")
print("Nice to meet, you " + name + ".")
time.sleep(1)
print("Here is your Pasta recipe:")
time.sleep(1)
recipe = ["Boil water", "Add salt", "Cook for 5 minutes", "Remove water", "Done!"]
for opr in recipe:
  print(opr)
  time.sleep(1)