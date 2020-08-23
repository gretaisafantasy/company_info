"""
File: customer.py
Resources to manage a customer's information
"""


class Customer(object):
    """Represents a customer"""

    def __init__(self, name, address, phone):
        """Constructor creates a customer with the given
        name, address, and phone number"""
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        """Returns the customer's name"""
        return self.name

    def set_address(self, address):
         """Set the customer's address"""
         self.address = address

    def get_address(self):
        """Returns the customer's address"""
        return self.address

    def set_phone(self, phone):
         """Set the customer's phone number"""
         self.phone = phone

    def get_phone(self):
        """Returns the customer's phone number"""
        return self.phone

    def __str__(self):
        """Returns the string representation of the customer"""
        return "Name: " + str(self.name) + "\n" + \
               "Address: " + str(self.address) + "\n" + \
               "Phone: " + str(self.phone)


