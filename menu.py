# Menu-driven program that runs until user chooses Exit

while True:
    # Display menu
    print("\n===== MAIN MENU =====")
    print("1. Add numbers")
    print("2. Generate multiplication table")
    print("3. Check even/odd numbers in a range")
    print("4. Convert data types")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    
    # Option 1: Add numbers
    
    if choice == "1":
        print("\n--- ADD NUMBERS ---")
        count = int(input("How many numbers do you want to add? "))

        total_sum = 0
        for i in range(count):
            num = float(input(f"Enter number {i+1}: "))
            total_sum += num

        print(f"Total sum: {total_sum}\n")

    
    # Option 2: Multiplication Table
    
    elif choice == "2":
        print("\n--- MULTIPLICATION TABLE ---")
        number = int(input("Enter a number: "))

        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    
    # Option 3: Even/Odd Checker
    
    elif choice == "3":
        print("\n--- EVEN/ODD CHECKER ---")
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))

        for n in range(start, end + 1):
            if n % 2 == 0:
                print(f"{n} is EVEN")
            else:
                print(f"{n} is ODD")

    
    # Option 4: Data Type Converter
    
    elif choice == "4":
        print("\n--- DATA TYPE CONVERTER ---")
        value = input("Enter any input: ")

        print("\nConversions:")

        # Convert to integer if possible
        try:
            print("Integer:", int(value))
        except ValueError:
            print("Integer: Cannot convert")

        # Convert to float
        try:
            print("Float:", float(value))
        except ValueError:
            print("Float: Cannot convert")

        # Convert to string (always possible)
        print("String:", str(value))

        # Convert to boolean
        print("Boolean:", bool(value))

    
    # Option 5: Exit Program
    
    elif choice == "5":
        print("\nExiting program. Goodbye!")
        break

    # Invalid choice handling
    else:
        print("\nInvalid choice. Please select a number from 1 to 5.")
