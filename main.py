# Adina Williams Student ID: 001830909
import csv
import datetime
import Package
from DataStructures import HashTable
from Package import Package
from Truck import Truck


# time-complexity -> O(N)
def load_package_data():
    """
    This function will load the package csv data into the package hash table. It will create a package object for each package item in the csv, and insert it into the hash table,
    """
    # load package csv data
    package_data = load_csv('packages.csv')
    for data in package_data:
        package_id = int(data[0])
        address = data[1]
        city = data[2]
        state = data[3]
        zipcode = int(data[4])
        deadline = data[5]
        mass = int(data[6])

        # package object
        package_list = Package(package_id, address, city, state, zipcode, deadline, mass, status="At Hub",
                               time_delivered=None, time_left_hub=None)
        # insert package data into hash table
        package_hash_table.insert(package_id, package_list)


# time-complexity -> O(N)
def load_csv(file_name, list_of_lists=True):
    """
    This function reads the csv file data and returns it as a list or a list of lists.

    :param file_name: The name of the csv file
    :param list_of_lists: Boolean to decide if returned list should be 2-D array or a list. Default True
    :return: csv data
    """

    csv_data_read = []
    with open(file_name) as file:
        csv_data = csv.reader(file, delimiter=',')
        if list_of_lists:
            csv_data_read = [row for row in csv_data]  # create 2-D array
        else:
            for row in csv_data:
                csv_data_read.extend(row)  # create list
    return csv_data_read


# Assign the hash table to a variable
package_hash_table = HashTable()
load_package_data()
# load the csvs for distances and addresses
distances = load_csv('distances.csv')
addresses = load_csv('addresses.csv', False)


# time complexity -> O(N^2)
# time complexity of entire program -> O(N^2)
def deliver_packages(truck):
    """
    This function will deliver the packages on a truck, based on the next closest address at every point in time.
    :param truck: The truck to deliver
    """
    starting_location = truck.current_address  # the starting location is the first address on the truck - the hub
    depart_hub_time = truck.current_time  # the hub depart time is the time first assigned to the truck
    while len(truck.packages) > 0:  # while there are still packages to deliver
        # the next stop is the package on the truck with the closest address to the truck's current address
        # the distance is the distance between the truck's current address and the closest package address
        next_stop, distance = minimum_distance(truck.current_address, truck.packages)
        truck.miles_traveled += distance  # increment the distance traveled on the truck
        time_to_deliver = distance / 18  # the amount of time to deliver the package in hours
        # find the truck's current time by adding the time it took to deliver the package
        truck.current_time += datetime.timedelta(hours=time_to_deliver)
        truck.current_address = next_stop  # swap the truck's current address to the current package address
        for package in list(truck.packages):  # for the packages on the truck
            if next_stop == package.address:  # find the current package
                truck.packages.remove(package)  # remove the current package from the truck
                package.time_left_hub = depart_hub_time  # package leaves hub at truck's depart time
                package.status = "Delivered"
                package.time_delivered = truck.current_time  # the package delivery time is the new truck time
                package_hash_table.insert(package.package_id, package)  # update the package in the hash table
            # at 10:20, update the address for package ID 9
            if truck.current_time >= datetime.timedelta(hours=int(10), minutes=int(20)) and package.package_id == 9:
                package.address = "410 S State St"
                package.zipcode = "84111"
                package_hash_table.insert(package.package_id, package)
    # get the distance between the hub and the last delivered package's address
    distance_to_hub = distance_between(truck.current_address, starting_location)
    truck.miles_traveled += distance_to_hub  # add the final trip to the hub to the total distance
    time_to_deliver = distance_to_hub / 18  # get the amount of time it took truck to travel to hub
    truck.current_time += datetime.timedelta(
        hours=time_to_deliver)  # update the truck's time with the time it returned to hub


# time-complexity -> O(N)
def minimum_distance(from_address, truck_packages):
    """
    This function returns the closest address and the distance between a given address and a list of package addresses.
    :param from_address: The address to compare too
    :param truck_packages: The list of packages
    :return: min_distance_address, min_distance
    """
    min_distance = None
    min_distance_address = None
    for package in truck_packages:  # for the addresses in the list of packages
        distance_between_address = distance_between(from_address, package.address)
        # sets the minimum distance to the closest distance of any package address to the from address
        # sets the address to that of the closest address to the from address
        if (min_distance is None or distance_between_address < min_distance) and distance_between_address > 0:
            min_distance = distance_between_address
            min_distance_address = package.address
    return min_distance_address, min_distance


# time-complexity -> O(1)
def distance_between(address1, address2):
    # calculate the distance between two addresses
    distance = distances[addresses.index(address1)][addresses.index(address2)]
    # gets the distance from the distances 2d array at distances[][]
    return float(distance)


# time-complexity -> O(N)
def load_truck(list_of_ids):
    """
    This function will take a list of package ID's and create a list of packages with those ID numbers only. This list will represent packages to be delivered on the truck.
    :param list_of_ids: The list of package ID's
    :return: List of packages
    """
    packages_to_deliver = []
    for packages_id in list_of_ids:
        # search the hash table for the packages
        list_packages = package_hash_table.search(packages_id)
        packages_to_deliver.append(list_packages)  # create a list of undelivered packages
    return packages_to_deliver


# initialize truck 1
# truck 1 is set to leave at 8:00, initial address is set to the hub address
truck1 = Truck(miles_traveled=0,
               packages=load_truck([13, 14, 15, 16, 19, 20, 39, 34, 21, 7, 29, 4, 40, 1, 30, 8]),
               current_address="4001 South 700 East",
               current_time=datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0)))
# deliver truck 1's packages
deliver_packages(truck1)

# initialize truck 2
# truck 2 is set to leave at 9:05, initial address is set to the hub address
truck2 = Truck(miles_traveled=0,
               packages=load_truck([3, 18, 36, 38, 6, 25, 28, 32, 37, 26, 31, 5, 27, 35, 10, 11]),
               current_address="4001 South 700 East",
               current_time=datetime.timedelta(hours=int(9), minutes=int(5), seconds=int(0)))
# deliver truck 2's packages
deliver_packages(truck2)

# initialize truck 3
# truck 3 is set to leave at the time that truck 1 returns to the hub, initial address is set to the hub address
truck3 = Truck(miles_traveled=0,
               packages=load_truck([2, 9, 33, 12, 17, 22, 23, 24]),
               current_address="4001 South 700 East",
               current_time=truck1.current_time)
# deliver truck 3's packages
deliver_packages(truck3)


# time-complexity -> O(1)
def total_mileage():
    # calculate the mileage of all 3 trucks
    total = truck1.miles_traveled + truck2.miles_traveled + truck3.miles_traveled
    return total


# time-complexity -> O(N^2)
def lookup_package_info(user_input_time, user_input_choice, package_select):
    """
    This function displays the information for packages chosen by the user. Based on the user's choice in the UI, it will show all packages at a chosen time, or it will show a single package at a chosen time.
    :param user_input_time: The time chosen by the user
    :param user_input_choice: The menu option chosen by the user
    :param package_select: The package selected by the user
    """
    packages = []
    hour, minute = map(int, user_input_time.split(':'))  # get the hour and minute from user input
    time_entered = datetime.timedelta(hours=hour, minutes=minute)  # create datetime variable using user input time
    # create a list of all the packages in the package hash table
    # this allows manipulation of package statuses to display them without altering the hash table
    for i in range(len(package_hash_table.table)):
        all_packages = package_hash_table.search(i + 1)
        packages.append(all_packages)

    print("-------------------------------------------------------")
    # user input choice 1 is to show all packages at a specific time
    if user_input_choice == "1":
        print("\nShowing information for all packages at {}".format(user_input_time))
        print("\n{:^15}| {:^65} | {:^12} | {:^10} | {:^15}".format("Package ID", "Address", "Weight (kgs)", "Deadline",
                                                                   "Status"))
        for package in packages:
            # concatenation of address for readability and formatting
            package_full_address = package.address + ", " + package.city + ", " + str(package.zipcode)
            # set the status of the package based on the user input time
            if package.time_delivered <= time_entered:
                package.status = "Delivered"
            elif package.time_left_hub < time_entered:
                package.status = "En Route"
            else:
                package.status = "At Hub"
            # if the status is delivered, display the package info with its delivery time
            if package.status == "Delivered":
                print("{:^15}| {:<65} | {:^12} | {:^10} | {:<10}at {}".format(
                    package.package_id, package_full_address, package.mass, package.deadline, package.status,
                    package.time_delivered))
            # else, display with no delivery time
            else:
                print("{:^15}| {:<65} | {:^12} | {:^10} | {:<10} ".format(
                    package.package_id, package_full_address, package.mass, package.deadline, package.status))

    # user input choice 2 is to show a single chosen package at a specific time
    elif user_input_choice == "2":
        print("\nShowing information for package ID '{}' at {}".format(package_select, user_input_time))
        print("\n{:^15}| {:^65} | {:^12} | {:^10} | {:^15}".format("Package ID", "Address", "Weight (kgs)", "Deadline",
                                                                   "Status"))

        for package in packages:
            if package.package_id == int(package_select):  # when user package ID choice is found
                package_full_address = package.address + ", " + package.city + ", " + str(package.zipcode)
                # set the status of the package based on user input time
                if package.time_delivered <= time_entered:
                    package.status = "Delivered"
                elif package.time_left_hub <= time_entered:
                    package.status = "En Route"
                else:
                    package.status = "At Hub"
                # if the status is delivered, display the package info with its delivery time
                if package.status == "Delivered":
                    print("{:^15}| {:<65} | {:^12} | {:^10} | {:<10}at {}".format(
                        package.package_id, package_full_address, package.mass, package.deadline, package.status,
                        package.time_delivered))
                # else, display with no delivery time
                else:
                    print("{:^15}| {:<65} | {:^12} | {:^10} | {:<10} ".format(
                        package.package_id, package_full_address, package.mass, package.deadline, package.status))


# time-complexity -> O(N)
def option_one_input():
    """
    This function is the UI for menu option 1. Show all packages at a specific time.
    """
    time_input = input("\nPlease enter a time using 24-Hour time format [HH:mm]: ")
    try:
        # display the information for the chosen time
        lookup_package_info(time_input, "1", package_select=None)
        no_continue = False
        # additional options after package information has displayed
        while not no_continue:
            continue_input = input(
                "\nWould you like to check for another time [1], go to main menu [2] or exit the program [exit]? ")
            # check for another time
            if continue_input == "1":
                option_one_input()
                no_continue = True
            # return to main menu
            elif continue_input == "2":
                main()
                no_continue = True
            # exit the program
            elif continue_input.lower() == "exit":
                print("Goodbye!")
                no_continue = True
                exit()
            # invalid input
            else:
                print("\nInvalid input, please try again using [1, 2 or 'exit']. ")
    except ValueError:
        print("\nIncorrect time format! Tip: please include the ':' ")
        option_one_input()


# time-complexity -> O(N)
def option_two_input():
    """
    This function is the UI for menu option 2. Show info for a specific package at a specific time.
    """
    try:
        package_choice = int(input("\nEnter the package ID you want to search [1-40]: "))
        # if invalid package chosen, choose again
        if package_choice > 40 or package_choice < 1:
            print("\nInvalid package ID. Choose an ID between 1-40. ")
            option_two_input()
        else:
            correct_time = False
            while not correct_time:
                try:
                    time_choice = input("\nEnter a time using 24-Hour time format [HH:mm]: ")
                    lookup_package_info(time_choice, "2", package_choice)
                    correct_time = True
                except ValueError:
                    print("\nIncorrect time format! Tip: please include the ':' ")

            no_continue = False
            # additional options after package info has displayed
            while not no_continue:
                continue_input = input("\n\nWould you like to: \n[1] Check for another package and time"
                                       "\n[2] Go to main menu"
                                       "\n[Exit] Exit the program\n")
                # check for another package & times
                if continue_input == "1":
                    option_two_input()
                    no_continue = True
                # return to main menu
                elif continue_input == "2":
                    main()
                    no_continue = True
                # exit the program
                elif continue_input.lower() == "exit":
                    print("\nGoodbye! Exiting program.")
                    exit()
                    no_continue = True
                # invalid input
                else:
                    print("\n Invalid input, please try again using [1, 2 or 'exit']. ")
    # exception if any other data type than an integer is entered for package ID choice
    except ValueError:
        print("\nInput error! Please enter integer value. ")
        option_two_input()


def main():
    # main UI
    print("\nWelcome to the WGUPS delivery information system!")
    first_input = input("\nWhat would you like to do? "
                        "\n1. View the status of all packages at a specific time. "
                        "\n2. View the status of a single package at a specific time. "
                        "\n3. View the total mileage travelled by all trucks. "
                        "\n\nEnter [1, 2, or 3] or type 'Exit' to exit the program. ")
    # option 1 - all packages, specific time
    if first_input == "1":
        option_one_input()
    # option 2 - specific package, specific time
    elif first_input == "2":
        option_two_input()
    # option 3- view total truck mileage
    elif first_input == "3":
        print("\nTotal mileage travelled by all trucks: ", total_mileage(), "miles")
        option_three_input = input("\nType [1] to return to the main menu. Type any other key to exit the program. ")
        # return to main menu
        if option_three_input == "1":
            main()
        # exit the program
        else:
            print("Goodbye! Exiting program. ")
            exit()
    # exit the program
    elif first_input.lower() == "exit":
        print("\nGoodbye! Exiting program. ")
        exit()
    else:
        print("\nInput Invalid. Please try again. ")
        main()


if __name__ == '__main__':
    main()
