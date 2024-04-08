class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
    def display_info(self):
        print("Vehicle type: ", self.vehicle_type)

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof_type):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof_type = roof_type
        
    def display_info(self):
        super().display_info()
        print("Year: ", self.year)
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Number of Doors 2 or 4: ", self.doors)
        print("Type of roof: ", self.roof_type)
        
def main():
    vehicle_type = "Car"
    car_year = input("Enter year: ")
    car_make = input("Enter make: ")
    car_model = input("Enter model: ")
    
    # Prompt for doors until a valid input is provided (2 or 4)
    while True:
        car_doors = input("Enter number of doors (2 or 4): ")
        if car_doors in ['2', '4']:
            break
        else:
            print("Invalid input. Please enter 2 or 4.")

    car_roof_type = input("Enter type of roof (solid or sun roof): ")
    
    car = Automobile(vehicle_type, car_year, car_make, car_model, car_doors, car_roof_type)
    print("\nCar Info: ")
    car.display_info()
        
if __name__== "__main__":
    main()
