
# File Name: automobile_info.py
# Author: Merhawi Gebrehiwot
# Description: This program prompts the user to input information about a car, including the year, make, model, number of doors, and type of roof. 
#              It then displays this information in a formatted manner.
# Variables:
#   vehicle_type: A string representing the type of vehicle (e.g., "Car").
#   car_year: A string representing the year of the car.
#   car_make: A string representing the make of the car.
#   car_model: A string representing the model of the car.
#   car_doors: A string representing the number of doors of the car (either "2" or "4").
#   car_roof_type: A string representing the type of roof of the car (either "solid" or "sun roof").
#   car: An instance of the Automobile class, representing the car object.
#   Vehicle: A class representing a generic vehicle with a display_info method.
#   Automobile: A subclass of Vehicle representing an automobile with additional attributes and a display_info method.

# Define the Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
    # Method to display vehicle type
    def display_info(self):
        print("Vehicle type: ", self.vehicle_type)

# Define the Automobile class, inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof_type):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type
        
    # Method to display automobile information
    def display_info(self):
        super().display_info()
        print("Year: ", self.year)
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Number of Doors 2 or 4: ", self.doors)
        print("Type of roof: ", self.roof_type)

# Define the main function
def main():
    # Initialize vehicle type
    vehicle_type = "Car"
    
    # Prompt user for car information
    car_year = input("Enter year: ")
    car_make = input("Enter make: ")
    car_model = input("Enter model: ")
    
    # Prompt user for number of doors until valid input is provided (2 or 4)
    while True:
        car_doors = input("Enter number of doors (2 or 4): ")
        if car_doors in ['2', '4']:
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    car_roof_type = input("Enter type of roof (solid or sun roof): ")
    
    # Create an instance of Automobile with user-provided information
    car = Automobile(vehicle_type, car_year, car_make, car_model, car_doors, car_roof_type)
    
    # Display car information
    print("\nCar Info: ")
    car.display_info()
        
# Check if the script is being run directly
if __name__== "__main__":
    main()

