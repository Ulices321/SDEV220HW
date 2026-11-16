class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

info = Automobile("Car", 2022, "Toyota", "Corolla", 4, "Sunroof")
print(f"Vehicle Type: {info.vehicle_type}")
print(f"Year: {info.year}")
print(f"Make: {info.make}")
print(f"Model: {info.model}")
print(f"Doors: {info.doors}")
print(f"Roof Type: {info.roof}")

