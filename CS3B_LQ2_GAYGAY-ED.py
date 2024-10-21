# Store the values of the student and classmate
students = {
    "student": {
        "name": "Lewis Fonsi",
        "address": "City of Candon, Ilocos Sur",
        "fav_num": 25,
        "age": 25,
        "allowance": 500.0
    },
    "classmate": {
        "name": "Andrea Andres",
        "address": "City of Vigan, Ilocos Sur",
        "fav_num": 18,
        "age": 21,
        "allowance": 700.0
    }
}

# Store the length of the studentName and classMate 
name_lengths = [len(students["student"]["name"]), len(students["classmate"]["name"])]

# Function containing the IF...ELIF...ELSE condition
def check_addresses_and_compare_names():
    student_name = students["student"]["name"]
    student_address = students["student"]["address"]
    classmate_name = students["classmate"]["name"]
    classmate_address = students["classmate"]["address"]

    sName_Length = name_lengths[0]
    cName_Length = name_lengths[1]

    if "Ilocos Sur" in student_address and "Ilocos Sur" in classmate_address:
        print(f"{student_name} is from {student_address}")
        print(f"{classmate_name} is from {classmate_address}")
        
        if sName_Length > cName_Length:
            print(f"{classmate_name} has a longer name than {student_name} with {cName_Length} letters over {sName_Length} letters")
        else:
            print(f"{student_name} has a longer name than {classmate_name} with {sName_Length} letters over {cName_Length} letters")
    else:
        print("None of the students live in Ilocos Sur")

# Function to calculate age and favorite number
def calculate_age_and_favnum():
    added_age = students["student"]["age"] + students["classmate"]["age"]
    print(f"The added age of {students['classmate']['name']} and {students['student']['name']} is {added_age}")
    
    sub_favnum = students["student"]["fav_num"] - students["classmate"]["fav_num"]
    print(f"The subtracted value of favnum of {students['classmate']['name']} and {students['student']['name']} is {sub_favnum}")

# Function to calculate weekly allowance
def calculate_combined_allowance():
    combined_weekly_allowance = students["student"]["allowance"] + students["classmate"]["allowance"]
    rounded_number = format(combined_weekly_allowance, ".2f")
    print(f"The weekly allowance of {students['classmate']['name']} and {students['student']['name']} is {rounded_number} pesos")

# Reverse the sort of the class Numbers 
class_numbers = [
    students["student"]["fav_num"],
    students["student"]["age"],
    int(students["student"]["allowance"]),
    students["classmate"]["age"],
    students["classmate"]["fav_num"],
    int(students["classmate"]["allowance"])
]

class_numbers.sort(reverse=True)
print("Reversed sorted classNumbers list:", class_numbers)

for value in class_numbers:
    print(value)

# Function for Quiz 2
def quizTwo(student_name_cs):
    print(f"Congratulations on Quiz 2, {student_name_cs}")

# Ask for User Input for the Name and pass it to quizTwo()
user_name = input("Please enter your name: ")
quizTwo(user_name)

# Function to execute the logic
check_addresses_and_compare_names()
calculate_age_and_favnum()
calculate_combined_allowance()
