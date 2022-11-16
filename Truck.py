# the truck class
class Truck:
    def __init__(self, packages, miles_traveled, current_address, current_time):
        self.current_time = current_time
        self.current_address = current_address
        self.miles_traveled = miles_traveled
        self.packages = packages

    def __str__(self):  # overwrite print(Truck) otherwise it will print object reference
        return "%s, %s, %s, %s" % (
            self.packages, self.miles_traveled, self.current_address, self.current_time)
