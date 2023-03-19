current_year = 2023
average_age = 18

def age_cal():
    age_calculation = int(input("enter year of birth: "))
    name = input("enter your name: ")
    if age_calculation < 2006:
        final_age = current_year - age_calculation
        print("hello", name, "your age is", final_age, "years")
    else:
        final_age = current_year - age_calculation
        print("sorry", name, "you are", final_age, "years old, expected age is 18 and above")

age_cal()        