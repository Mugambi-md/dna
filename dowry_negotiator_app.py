def body_count(age, asked_dowry):
    "Determines body count based on age"
    if age < 18:
        return 5
    elif age < 20:
        return 7
    elif age <25:
        return 10
    elif age < 30:
        return 15
    else:
        return asked_dowry-1
    

def dowry_negotiation(name, body_count_result, asked_dowry, college):
    if college:
        body_count_result = body_count_result * 1.5
    else:
        body_count_result = body_count_result
    
    actual_dowry = asked_dowry/(body_count_result + 1)

    print(f"Recomeded Dowry for: {name} is {actual_dowry}")

def get_user_data():
    """Function to collect user data and pass it to the processing function."""
    name = input("Enter Brides Name: ")
    age = int(input("Enter Brides' Age: "))
    asked_dowry =int(input("Enter the dowry requested: "))
    
    college_input = input("Has she gone to college? (yes/no): ").strip().lower()
    while college_input not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        college_input = input("Has she gone to college?(yes/no): ")
    college = college_input=="yes"
    body_count_result = body_count(age, asked_dowry)
    dowry_negotiation(name, body_count_result, asked_dowry, college)


if __name__ == "__main__":
    print("Welcome to dowry negotiation program!")
    get_user_data()