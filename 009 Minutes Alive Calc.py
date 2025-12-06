"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""


def calculate_minutes_alive(age_years):
    days_per_year = 365.25
    total_days = age_years * days_per_year
    total_hours = total_days * 24
    total_minutes = total_hours * 60
    return round(total_days), round(total_hours), round(total_minutes)
  

while True:
    try:
        age_input = input("Enter your age in years (or type 'exit' to quit): ")
        if age_input.lower() == 'exit':
            print("Goodbye!")
            break

        age_years = float(age_input)
        days, hours, minutes = calculate_minutes_alive(age_years)

        print(f"You are approximately:")
        print(f"  - {days:,} days old")
        print(f"  - {hours:,} hours old")
        print(f"  - {minutes:,} minutes old")
    except ValueError:
        print("Please enter a valid number for your age.")
        
