"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_log.csv"

def visualise_weather():
    dates = []
    temperatures = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", newline="", encoding="cp1252") as file:
        reader = csv.DictReader(file)

        reader.fieldnames = [name.strip() for name in reader.fieldnames]

        for row in reader:
            try:
                dates.append(row["Date"])
                temperatures.append(float(row["Temperature"]))
                conditions[row["Condition"]] += 1
            except (ValueError, KeyError):
                continue

    if not dates:
        print("No data available to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker="o")
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(7, 4))
    plt.bar(conditions.keys(), conditions.values())
    plt.title("Weather Conditions Frequency")
    plt.xlabel("Condition")
    plt.ylabel("Number of Days")
    plt.tight_layout()
    plt.show()


visualise_weather()
