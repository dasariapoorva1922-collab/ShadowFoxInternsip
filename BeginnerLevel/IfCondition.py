#4.If Conditions

#1.Calculate BMI and categorize it
def calculate_bmi():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmi = weight / (height ** 2)
    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"
    
    print(f"Your BMI is {bmi:.2f}, which is categorized as: {category}")

#2.Determine which country a city belongs to
def find_country():
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
    city = input("Enter a city name: ")

    if city in australia:
        print(f"{city} is in Australia")
    elif city in uae:
        print(f"{city} is in UAE")
    elif city in india:
        print(f"{city} is in India")
    else:
        print(f"{city} is not in our database")

#3.check if two cities belongs to the same country
def check_same_country():
    australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")

    if (city1 in australia and city2 in australia) or \
       (city1 in uae and city2 in uae) or \
       (city1 in india and city2 in india):
        print("Both cities are in the same country")
    else:
        print("They don't belong to the same country")
# Run the functions
print("Task 1: BMI Calculation")
calculate_bmi()
print("\nTask 2: Find Country of a City")
find_country()
print("\nTask 3: Check if Two Cities Belong to the Same Country")
check_same_country()
