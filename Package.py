# the package class
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, mass, status, time_delivered, time_left_hub):
        self.time_left_hub = time_left_hub
        self.time_delivered = time_delivered
        self.status = status
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.mass = mass

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.package_id, self.address, self.city, self.state, self.zipcode, self.deadline, self.mass,
            self.status, self.time_delivered)



