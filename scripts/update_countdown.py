#!/usr/bin/env python3
from datetime import datetime, date

TARGET_DATE = date(2026, 2, 18)
README_PATH = "README.md"

def generate_content(days_left):
    if days_left > 1:
        message = f"**{days_left} days until I see skyy** 💫"
    elif days_left == 1:
        message = f"**1 day until I see skyy** 💫"
    elif days_left == 0:
        message = "**Today I see skyy!** 🎉"
    else:
        # After the date has passed, count upwards
        days_after = abs(days_left)
        message = f"**+{days_after} days maybe I get to see her** 💭"
    
    content = f"{message}\n"
    return content

def main():
    today = date.today()
    days_left = (TARGET_DATE - today).days
    content = generate_content(days_left)
    
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated countdown: {days_left} days remaining")

if __name__ == "__main__":
    main()
