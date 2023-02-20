from datetime import datetime

birthday_str = input("Enter your birthday (mm/dd/yyyy): ")

birthday = datetime.strptime(birthday_str, '%m/%d/%Y')

age_seconds = (datetime.now() - birthday).total_seconds()

print("You are approximately", int(age_seconds), "seconds old.")
