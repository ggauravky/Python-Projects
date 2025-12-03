"""
 Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""
from datetime import date

def generate_self_intro(): 
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    profession = input("Enter your profession: ")
    hobby = input("Enter your favorite hobby: ")

    intro_paragraph = (f"Hello! My name is {name}. I'm {age} years old and live in {city}. "
                       f"I work as a {profession} and I absolutely enjoy {hobby} in my free time. "
                       "Nice to meet you!")

    current_date = date.today().isoformat()
    intro_paragraph += f"\nLogged on: {current_date}"


    border = '*' * (len(intro_paragraph.split('\n')[0]) + 4)
    
    print(border)
    print(f"* {intro_paragraph} *")
    print(border)

generate_self_intro()