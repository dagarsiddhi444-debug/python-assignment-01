# Name: Siddhi Dagar
# Roll No: 2501060046
# Course: BCA
# Semester: 1st
# Subjest: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Tittle: Student Profile Console App


# Task 1: Introduction
print("Welcome to the Student Profile Console App")
print("This tool helps you to create a formatted student profile")
print()
print()

#Task 2: Input & Variables
name = input("Enter your full name: ")
roll_no = int(input("Enter your roll number: "))
program = input("Enter your program (e.g., BCA:")
university = input("Enter your university name: ")
city = input("Enter your city:")
age = int(input("Enter your age:"))
hobby = input("Enter your hobby:")
print()
print()

# Task 3: Operators Demonstration
print("Demonstrating Python Operators:")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(f"Addition: {num1}+{num2} = {num1 + num2}")
print(f"Sbubtraction: {num1}-{num2} = {num1 - num2}")
print(f"multiplicatiom: {num1}*{num2} = {num1 * num2}")
print(f"Division: {num1}/{num2} = {num1 / num2}")
print(f"Modulus: {num1}%{num2} = {num1 % num2}")
print(f"Exponentiation: {num1}**{num2} = {num1 ** num2}")
print(f"Floor Division: {num1}//{num2} = {num1 // num2}")
print()
print()

# Task 4: Formatted Output
print("\n--- String Operations ---")
print("Concatenation:", name + " - " + city)
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Replace:", name.replace("a", "@"))
print("Count of 'a':", name.count("a"))
print()
print()

# Task 5: Final Output — Student Profile Card
print("\n----------------------------------------")
print("STUDENT PROFILE SYSTEM")
print("----------------------------------------")
print(f"Name:       {name}")
print(f"Roll No:    {roll_no}")
print(f"Course:     {program}")
print(f"University: {university}")
print(f"City:       {city}")
print(f"Age:        {age}")
print(f"Hobby:      {hobby}")
print("----------------------------------------")
print("Welcome to Python Programming !")
print()
print()

# Task 6: Bonus Task
save_choice = input("\nDo you want to save your profile? (yes/no): ")
if save_choice.lower() == "yes":
    with open("student_profile.txt", "w") as f:
        f.write(f"Name: {name}\nRoll No: {roll_no}\nCourse: {program}\n"
                f"University: {university}\nCity: {city}\nAge: {age}\nHobby: {hobby}\n")
    print("Profile saved to student_profile.txt")