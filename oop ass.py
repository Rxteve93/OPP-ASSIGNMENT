class Smartphone:
    def __init__(self, brand, model, storage_capacity):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity
        self.battery_level = 100
        self.is_charging = False

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo.")

    def play_game(self, game_name):
        print(f"{self.brand} {self.model} is playing {game_name}.")

    def charge(self):
        if not self.is_charging:
            print(f"{self.brand} {self.model} started charging.")
            self.is_charging = True
        else:
            print(f"{self.brand} {self.model} is already charging.")

    def check_battery(self):
        print(f"{self.brand} {self.model}'s battery level is {self.battery_level}%.")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_capacity, cooling_system):
        super().__init__(brand, model, storage_capacity)
        self.cooling_system = cooling_system
        self.performance_boost = False

    def boost_performance(self):
        if not self.performance_boost:
            print(f"{self.brand} {self.model}'s {self.cooling_system} is activated for boosted performance!")
            self.performance_boost = True
        else:
            print(f"{self.brand} {self.model}'s performance is already boosted.")

# Creating instances of the classes
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB")
phone2 = GamingSmartphone("ROG", "Phone 7", "512GB", "Vapor Chamber")

# Using the methods
phone1.call("08012345678")
phone1.take_photo()
phone1.charge()
phone1.check_battery()
print("-" * 20)
phone2.play_game("Asphalt 9")
phone2.boost_performance()
phone2.charge()
phone2.check_battery()
