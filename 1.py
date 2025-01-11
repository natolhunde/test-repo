import datetime
# This imports the datetime module from Python's standard library.
# It provides classes for working with dates and times.
# We'll use it to get the current year for age calculations.
def get_valid_year(prompt): # This function is defined to ensure a valid year input.
    while True:
        try:
            year = int(input(prompt))
            if 1900 <= year <= datetime.datetime.now().year:
                return year
            else:
                print("Please enter a valid year between 1900 and the current year.")
        except ValueError:
            print("Please enter a valid number for the year.")

# Parameters:
# prompt: The message to display when asking for input.
def get_valid_age(prompt, max_age):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= max_age:
                return age
            else:
                print(f"Please enter a valid age between 0 and {max_age}.")
        except ValueError:
            print("Please enter a valid number for age.")

# Print greeting
print("Hello User!")

# Ask for name
name = input("What is your name? ").strip()
print(f"Hello {name}")

# Ask for year of birth
birth_year = get_valid_year("What is your year of birth? ")

# Calculate current year and age
current_year = datetime.datetime.now().year
age = current_year - birth_year

# Ask about driving
while True:
    can_drive = input("Do you know how to drive? (Yes/No) ").lower().strip()
    if can_drive in ['yes', 'no']:
        break
    print("Please answer 'Yes' or 'No'.")

if can_drive == "yes":
    license_age = get_valid_age(f"How old were you when you got your driving license? (0-{age}) ", age)
    license_year = birth_year + license_age
    driving_years = current_year - license_year
    print(f"You got your driving license in {license_year} and you have been driving for {driving_years} years")
else:  # can_drive == "no"
    if age > 30:
        supposed_license_year = birth_year + 30
        years_ago = current_year - supposed_license_year
        print(f"You are {age} years old now but you still can't drive. You were supposed to get your license in {supposed_license_year}, {years_ago} years ago at the age of 30 at the latest")
    else:
        years_to_30 = 30 - age
        license_year = current_year + years_to_30
        print(f"You are {age} years old now and you should work on getting your driving license before you turn 30. You have {years_to_30} years to go until the year {license_year}")
