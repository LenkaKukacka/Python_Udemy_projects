pizza_list = ["margarita", "cheesy", "peperoni", "napoli", "rusticana"]
order_list = []
bill = 0
pizza_price = 10
tips = 0

order_start = input("Would you like to add pizza to your order? yes/no  ")
print()
while order_start == "yes":
    print("Here is our offer:")
    for i, pizza in enumerate(pizza_list):
        print(str(i + 1) + ". " + pizza)
    print()
    # musis tou petkou zavolat list a priradit string do noveho seznamu
    # print(pizza_list[int(pizza) - 1]) #test: přiřazuji jmeno pizzy k inputu čisla

    valid_pizza = False
    while not valid_pizza:
        pizza = int(input("Choose number from 1 to 5 according to the pizza you want to add.  "))
        if pizza >= 0 and pizza < 6:
            order_list.append(pizza_list[int(pizza) - 1])
            print("Your order now include: " + str(order_list))
            bill += pizza_price
            print("your bill is: " + str(bill) + " EUR")
            print()
            valid_pizza = True
        else:
            print("Please, provide correct number from our offer.")

    order_start = input("Would you like to add pizza to your order? yes/no  ")

if order_start == "no" and bill != 0:
    print("Okay. You order is following: " + str(order_list))
    print()
    ask_tips = input("Would you like to add tips? yes/no  ")
    if ask_tips == "yes":
        tips = float(input("How much tips you want to give in range 0-25 ?"))
        total_price = bill + ((tips / 100) * bill)
        print()
        print("Your total price is incl. tips: " + str(total_price) + " EUR.\nThank you for your order :)")
    else:
        # if ask_tips == "no":
        print("Your total price is: " + str(bill) + " EUR.\nThank you for your order :) ")

else:
    exit()