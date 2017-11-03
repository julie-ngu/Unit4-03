# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This is a program that lets the user input their address and prints it out

def print_address(street_address, city, province, postal_code, apartment = ''):
    # prints address
    if apartment == '':
        print(street_address + ' ' + city + ' ' + province + ' ' + postal_code)
    else:
        print(street_address + ' ' + city + ' ' + province + ' ' + postal_code + ' ' + apartment_number)

street_address = raw_input("Enter your street address: ")
city = raw_input("Enter the name of your city: ")
province = raw_input("Enter the name of your province: ")
postal_code = raw_input("Enter your postal code: ")
apartment_number_option = raw_input("Do you have an apartment number?(y/n): ")

if apartment_number_option == 'y':
    apartment_number = raw_input("Enter your apartment number: ")
    print_address(street_address, city, province, postal_code, apartment = apartment_number)
else:
    print_address(street_address, city, province, postal_code)
