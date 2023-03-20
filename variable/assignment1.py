current_year = 2023
average_age = 18

def age_cal():
    name = input("enter your name: ")
    age_calculation = int(input("enter year of birth: "))
    final_age = current_year - age_calculation 
    if age_calculation < 2006:
        print("hello", name, "your age is", final_age, "years")
    else:
        print("sorry", name, "you are", final_age, "years old, expected age is 18 and above")

age_cal()        
