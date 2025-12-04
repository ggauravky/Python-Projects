"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

name=input("Enter your Name: ").strip()
profession=input("Enter your Profession: ").strip()
passion=input("Enter your one-liner passion or goal: ").strip()
emoji=input("Enter your favorite emoji (optional): ").strip()
website=input("Enter your Website or handle (optional): ").strip()

print("\nChoose a layout style:")
print("1. Classic")
print("2. Modern")
print("3. Minimalist")
style_choice=input("Enter the number corresponding to your choice (1/2/3): ").strip()

def generate_bio(style):
    if style == '1':
        bio_lines = []
        if emoji:
            bio_lines.append(f"{emoji} {name} | {profession}")
        else:
            bio_lines.append(f"{name} | {profession}")
        bio_lines.append(f"💡 {passion}")
        if website:
            bio_lines.append(f"🔗 {website}")
        return "\n".join(bio_lines)
    elif style == '2':
        bio_lines = []
        if emoji:
            bio_lines.append(f"{emoji} {name} - {profession}")
        else:
            bio_lines.append(f"{name} - {profession}")
        bio_lines.append(f"Passionate about: {passion}")
        if website:
            bio_lines.append(f"Find me at: {website}")
        return "\n".join(bio_lines)
    elif style == '3':
        bio_lines = []
        if emoji:
            bio_lines.append(f"{emoji} {name}")
        else:
            bio_lines.append(f"{name}")
        bio_lines.append(f"{profession} | {passion}")
        if website:
            bio_lines.append(f"{website}")
        return "\n".join(bio_lines)
    else:
        return "Invalid style choice."
    
bio = generate_bio(style_choice)
print("\nGenerated Bio:\n")
print(bio)
save_choice = input("\nDo you want to save the bio to a .txt file? (yes/no): ").strip().lower()
if save_choice == 'yes':
    filename = input("Enter the filename (without extension): ").strip() + ".txt"
    with open(filename, 'w') as file:
        file.write(bio)
    print(f"Bio saved to {filename}")