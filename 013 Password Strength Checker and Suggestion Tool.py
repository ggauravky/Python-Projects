"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import random
import string
import getpass

def check_pass_strength(passward):
    issues=[]
    if len(passward)<8:
        issues.append("too short , min 8 char")
    if not any(c.islower() for c in passward):
        issues.append("missing lowercase letter")
    if not any(c.isupper() for c in passward):
        issues.append("missing lowercase letter")
    if not any(c.isdigit() for c in passward):
        issues.append("missing digit letter")
    if not any(c in string.punctuation for c in passward):
        issues.append("missing special char")
    return issues

def generate_strong_pass(length=12):
    char=string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(char) for _ in range(length))

password=getpass.getpass("enter a pass:")
issues=check_pass_strength(password)

if not issues:
    print("strong password")
else:
    print("weak pass..")
    for issue in issues:
        print(f"-{issues}")

sugg=generate_strong_pass()
print("\n suggesting strong pass...")
print(sugg)