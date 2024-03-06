import time

print("Hello.")
time.sleep(1)
user_name = input("What is your name?")
print("Nice to meet, you " + user_name + ".")
#print(type(user_name))
time.sleep(1)
user_age = int(input("How old are you?")) #před inputem muzes definovat druh data, jestli odpoved bude zaznamenana jako int, str, nebo float. Stejně tak v printu pred variablem pred vypisem
time.sleep(1)
print("So, in 10 years you will be " + str(user_age+10) + "\n")

number_1 = int(input("Give me number 1: "))
number_2 = int(input("Give me number 2: "))
sum_1_2 = number_1+number_2
print("\n")
print("The sum of your numbers is: " + str(sum_1_2))


#Aktivita:
#import time
print("Activity: Study hours.")
print()
print( "Hello! Let´s have a look how many hours you can study this course!\n")
time.sleep(2)
print("Tell me something about you:\n")
time.sleep(2)

#inputs of hrs.
week_sleeping_hrs = float(input(
  "How many hours you sleep daily per week?\n"))#student needs to use "." in number they answear, eg. 6,5 is incorrect
week_working_hrs = float(input(
  "How many hours you work per day? Include commuting.\n"))
week_relax_hrs = float(input(
  "How many hours you would like to relax per day after work?\n"))
weekend_sleeping_hrs = float(input(
  "How many hours you sleep per day at the weekend?\n"))
weekend_relax_hrs = float(input(
  "How many hours you would like to do just nothing at the weekend day?\n"))

#Calculations
Available_week_day = 24 - (week_sleeping_hrs + week_working_hrs + \
                          week_relax_hrs + 3)
Available_sum_week = Available_week_day * 5
Available_weekend_day = 24 - (weekend_sleeping_hrs + \
                               weekend_relax_hrs + 3)
Available_sum_weekend = Available_weekend_day * 2
Available_sum_total = Available_sum_week + Available_sum_weekend

#Prints
print("\n")
print(
  "From Monday to Friday you have got " + str(Available_sum_week) + "hrs. weekly to study.\n")
print(
  "At the weekend you can have " + str(Available_sum_weekend) + " hrs. studying.\n")
print(
  "So, in total you can study this course: " + str(Available_sum_total) + "hrs. per whole week.")