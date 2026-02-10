def main():
    #Collect Input for each
    first = input("Child's First Name: ")
    
    last = input("Child's Last Name: ")
    
    print(f"Camper's Name: {first} {last}")

    birth = int(input(f"In what year was {first} {last} born: "))
    
    print(f"Birth Year: {birth}")

    days = int(input(f"How many days will {first} attend? "))
    
    print(f"Camp Duration: {days} days")

    p_first = input("Parent's First Name: ")
    
    p_last = input("Parent's Last Name: ")
    
    print(f"Parent's Name: {p_first} {p_last}")

    phone = input("Parent's Phone #: ")
    
    print(f"Phone Number: {phone}")

    street = input("Street Address: ")
    
    city = input("City: ")
    
    state = input("State Abbreviation: ")
    
    zip = input("Zip Code: ")
    
    print(f"Address:\n{street}\n{city}, {state} {zip}")

if __name__ == "__main__":
    main()
