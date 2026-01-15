"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
import requests
from datetime import datetime

FILENAME = "weather_log.csv"
API_KEY = "API_KEY"

if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "City", "Temperature (°C)", "Weather Condition"])


def log_weather():
    city = input("Enter city name: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")
    # Check for duplicate entry
    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print(f"Weather data for {city} on {date} already logged.")
                return
    # Fetch weather data from API
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(
                f"Error fetching data for {city}: {data.get('message', 'Unknown error')}"
            )
            return
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        # Log data to CSV
        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, city, temperature, condition])
        print(f"Logged weather data for {city} on {date}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_logs():
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            logs = list(reader)
            if len(logs) <= 1:
                print("No weather logs available.")
                return
            print(
                f"{'Date':<12} {'City':<20} {'Temperature (°C)':<18} {'Weather Condition':<20}"
            )
            print("-" * 70)
            for row in logs[1:]:
                print(f"{row[0]:<12} {row[1]:<20} {row[2]:<18} {row[3]:<20}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        print("\nWeather Logger Menu:")
        print("1. Add new weather log")
        print("2. View all logs")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            log_weather()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
