"""
File: company.py
Author: Greta Tanudjaja
Date: 7/14/2020
Defines classes for an Employee and Customer using inheritance.
"""

# Import the Person class from the person.py module
from person import Person

class Employee(Person):
    """Represents an employee"""

    def __init__(self, name, address, phone, badge, salary):
        """Constructor creates an Employee with the given
        name, address, phone, badge, and salary"""
        Person.__init__(self, name, address, phone)
        self._badge = badge
        self._salary = salary

    def set_badge(self, badge):
        """Set the employee's badge number"""
        self._badge = badge

    def get_badge(self):
        """Returns the employee's badge number"""
        return self._badge

    def set_salary(self, salary):
        """Set the employee's salary"""
        self._salary = salary

    def get_salary(self):
        """Returns the employee's salary"""
        return self._salary

    def __str__(self):
        """Returns the string representation of the employee"""
        return "name: " + str(self.get_name()) + "\n" + \
               "address: " + str(self.get_address()) + "\n" + \
               "phone: " + str(self.get_phone()) + "\n" + \
               "badge: " + str(self._badge)

    def __eq__(self, other):
        """Tests self and other for equality"""
        # Returns true if self and other point to the same object and if they
        # are 2 different objects, but have the same badge number
        if self is other and self._badge == other._badge:
            return True
        
class Customer(Person):
    """Represents a customer"""

    def __init__(self, name, address, phone, credit_score):
        """Constructor creates a Customer with the given
        name, address, phone, and credit score"""
        Person.__init__(self, name, address, phone)
        self._credit_score = credit_score

    def set_credit_score(self, credit_score):
        """Set the customer's credit score"""
        self._credit_score = credit_score

    def get_credit_score(self):
        """Returns the customer's credit score"""
        return self._credit_score

    def __str__(self):
        """Returns the string representation of the customer"""
        return "name: " + str(self.get_name()) + "\n" + \
               "address: " + str(self.get_address()) + "\n" + \
               "phone: " + str(self.get_phone()) + "\n" + \
               "credit_score: " + str(self._credit_score)

        
