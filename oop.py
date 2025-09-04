# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Public attribute
        self.model = model
        self._battery_life = battery_life  # Encapsulated attribute (protected)

    def display_info(self):
        print(f"{self.brand} {self.model} with {self._battery_life} hours battery life")

    def use(self):
        print(f"{self.brand} {self.model} is being used.")

    # Encapsulation: getter for battery life
    def get_battery_life(self):
        return self._battery_life

    # Encapsulation: setter with validation
    def set_battery_life(self, hours):
        if hours > 0:
            self._battery_life = hours
        else:
            print("Battery life must be positive.")

# Subclass: GamingPhone inherits from Smartphone showcasing inheritance and polymorphism
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)
        self.cooling_system = cooling_system

    # Polymorphism: override use() method
    def use(self):
        print(f"{self.brand} {self.model} is gaming with {self.cooling_system} cooling system.")

# Polymorphism Challenge: Different move() methods for Vehicle classes
class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Testing the classes and polymorphism
phone = Smartphone("Apple", "iPhone 13", 18)
phone.display_info()
phone.use()
print("Battery life:", phone.get_battery_life())
phone.set_battery_life(20)
print("Updated battery life:", phone.get_battery_life())

gaming_phone = GamingPhone("ASUS", "ROG Phone 5", 10, "Active Cooling")
gaming_phone.display_info()
gaming_phone.use()

vehicles = [Car(), Plane()]
for v in vehicles:
    v.move()  # Demonstrates polymorphism with same move() method behaving differently
