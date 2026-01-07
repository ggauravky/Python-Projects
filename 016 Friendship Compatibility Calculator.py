"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def calculate_compatibility(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    # Count shared letters
    shared_letters = set(name1) & set(name2)
    shared_count = sum(min(name1.count(letter), name2.count(letter)) for letter in shared_letters)

    # Count vowels
    vowels = 'aeiou'
    vowel_count = sum(1 for letter in name1 + name2 if letter in vowels)

    # Count matching character positions
    position_matches = sum(1 for a, b in zip(name1, name2) if a == b)

    # Calculate compatibility score
    score = (shared_count * 3 + vowel_count * 2 + position_matches * 5) % 101
    return score

def get_message_and_advice(score):
    if score >= 80:
        return ("You're like chai and samosa — made for each other! ☕️🥟", "Keep nurturing this beautiful friendship! 🌟")
    elif score >= 50:
        return ("You two have a solid bond! 🤝", "Spend more time together to strengthen your friendship! 😊")
    else:
        return ("Well... opposites attract, maybe? 🤔", "Embrace your differences and learn from each other! 🌈")

def framed_output(message, advice):
    full_message = f"{message}\n{advice}"
    lines = full_message.split('\n')
    width = max(len(line) for line in lines) + 4
    border = '+' + '-' * (width - 2) + '+'
    
    print(border)
    for line in lines:
        print(f"| {line.center(width - 4)} |")
    print(border)

def main():
    print("Welcome to the Friendship Compatibility Calculator! 🤗")
    name1 = input("Enter the name of Friend A: ")
    name2 = input("Enter the name of Friend B: ")

    score = calculate_compatibility(name1, name2)
    message, advice = get_message_and_advice(score)
    framed_output(message, advice)

if __name__ == "__main__":
    main()
    