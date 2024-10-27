# Function to convert inches to centimeters
def inches_to_cm(inches):
    cm = inches * 2.54
    return cm

# Main program
def main():
    print("Inches to Centimeters Converter")
    try:
        inches = float(input("Enter the length in inches: "))
        centimeters = inches_to_cm(inches)
        print(f"{inches} inches is equal to {centimeters:.2f} cm")
    except ValueError:
        print("Please enter a valid number.")

# Run the main program
if __name__ == "__main__":
    main()
