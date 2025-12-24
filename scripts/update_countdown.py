#!/usr/bin/env python3
from datetime import datetime, date

TARGET_DATE = date(2026, 2, 18)
README_PATH = "README.md"

def generate_content(days_left):
    if days_left > 1:
        countdown_text = f"{days_left} days"
    elif days_left == 1:
        countdown_text = "1 day"
    elif days_left == 0:
        countdown_text = "Today is the day"
    else:
        countdown_text = "The day has passed"
    
    if days_left > 0:
        message = f"**{countdown_text} until I see skyy** 💫"
    else:
        message = "**Finally seeing skyy!** 🎉"
    
    content = f"""# Countdown to February 18, 2026

{message}

---

*Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p IST')}*
"""
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
