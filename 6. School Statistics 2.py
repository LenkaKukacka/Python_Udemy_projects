grades = []
def get_user_grade(): # pokud si nevytvoris list uvnitr funkce, ztratili se ti list globalni funkce a kod nize nebude mit co volat
    grades = []
    ask_for_grades = True
    while ask_for_grades:
        grade = float(input("Give me your grade, please? 0-10 // To stop provide -1: "))
        if grade == -1:
            ask_for_grades = False
        else:
            if grade >= 0 and grade <= 10:
                grades.append(grade)
            else:
                print("Please, provice correct grade from 0 to 10!")
    return grades
def get_minimum(number_list):
    minimum = number_list[0]
    for number in number_list:
        if number < minimum:
            minimum = number
    return minimum
def get_maximum(number_list):
    maximum = number_list[0]
    for number in number_list:
        if number > maximum:
            maximum = number
    return maximum
def get_average(number_list):
    average = sum(number_list)/len(number_list)
    return average

grades = get_user_grade()
if len(grades) == 0:
    print("You have not provided any grade.")
    exit()
else:
    print("You have provided " + str(len(grades)) + " grades.")
    print(grades)
    minimum = get_minimum(grades)
    maximum = get_maximum(grades)
    average = get_average(grades)
    print("Minimum: " + str(minimum) + \
          "  Maximum: " + str(maximum) + \
          "  Average: " + str(average) )



