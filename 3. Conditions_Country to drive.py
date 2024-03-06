country = input("What country you would like to go?")
country_list = ["South Africa", "India", "France", "Mexico"]
# if country in country.list

if country in country_list:
    user_age = float(input("How old are you?"))

else:
    print("Sorry, this country is not included.")

if country == "South Africa":
    print("OK")
    if user_age >= 17:
        print("Okay, you can drive in the South Africe.")
    else:
        print("Sorry, you cannot drive in the South Africa.")

elif country == "France":
    # user_age = float(input("How old are you?"))
    if user_age >= 18:
        print("Okay, you can drive in France.")
    elif user_age >= 15:  # and user_age <18: #omezovani z obou stran nemusis resit, protoze python jde po radcich, pokud neni pravda ze je vetsi roven 16, koukne se jeste na vetsi rovno 15)
        print("You need to have supervision with you to drive in France.")
    else:
        print("Sorry, you cannot drive in France.")

elif country == "Mexico":
    # user_age = float(input("How old are you?"))
    if user_age >= 18:
        print("Okay, you can drive in Mexico.")
    elif user_age == 16 and user_age < 18:
        print("You need to have parental agreement to drive in Mexico.")
    elif user_age == 15:
        print("You need to have parental supervision to drive in Mexico.")
    else:
        print("Sorry, you cannot drive in Mexico.")

elif country == "India":
    # user_age = float(input("How old are you?"))
    if user_age >= 18:
        print("Okay, you can drive in India.")
    else:
        print("Sorry, you cannot drive in India.")