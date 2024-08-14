"""
account_holder is a regular attribute. You can access and modify it directly.

_balance is also an attribute, but the underscore convention suggests it's meant for internal use.
balance is a property. It provides controlled access to the _balance attribute:

The getter method allows you to retrieve the balance.

The setter method includes validation to prevent setting a negative balance.

The deposit and withdraw methods use the balance property's setter to modify the _balance attribute, ensuring the validation logic is applied.

Properties add a layer of abstraction and control over attribute access, enhancing code maintainability and preventing invalid data states.

General Benefits of Using Classes

Encapsulation: Classes bundle data (attributes) and the operations that can be performed on that data (methods) into a single unit. This helps in organizing code, making it easier to understand and maintain.

Abstraction: Classes provide a way to abstract away complex implementation details, presenting a simpler interface to the user. This reduces the cognitive load on the user, allowing them to focus on how to use the object rather than how it works internally.

Reusability: Once you define a class, you can create multiple instances (objects) of that class, each with its own state. This promotes code reusability, saving you from writing repetitive code.

Inheritance: Classes support inheritance, allowing you to create new classes (subclasses) that inherit properties and behaviors from existing classes (superclasses). This facilitates code reuse and helps establish relationships between different types of objects.

Polymorphism: Objects of different classes can respond to the same message (method call) in their own way. This allows you to write more generic and flexible code that can work with various types of objects.


The BankAccount class encapsulates all the data (account holder's name, balance) and the operations related to a bank account (deposit, withdraw) within a single unit.
By using a property with a setter method for the balance, we ensure that the balance cannot be set to a negative value. This protects the integrity of the account data.


Abstraction

The BankAccount class provides a simplified interface for interacting with a bank account. The user doesn't need to know how the balance is stored or updated internally; they just use the deposit and withdraw methods.


Reusability

You can create multiple BankAccount objects, each representing a different account with its own account holder and balance. This allows you to model multiple bank accounts in your program.


Potential for Extensibility

If you needed to create different types of bank accounts (e.g., savings accounts, checking accounts) with slightly different behaviors, you could create subclasses of BankAccount and add or override methods as needed. This provides a structured way to extend the functionality of your code.


Readability

The class-based approach makes the code more self-documenting. The class name (BankAccount) and method names (deposit, withdraw) convey their purpose, making the code easier to understand and maintain.
Overall, using a class in the BankAccount example leads to code that is:

"""
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Attribute
        self._balance = initial_balance  # Attribute (using underscore convention for "private")

    @property
    def balance(self):  # Property (getter)
        return self._balance

    @balance.setter
    def balance(self, amount):  # Property (setter)
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Using the setter to modify the balance
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount  # Using the setter
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Create an account
my_account = BankAccount("John Doe", 1000)

# Access attributes directly
print(my_account.account_holder)  # Output: John Doe

# Access balance using the property
print(my_account.balance)  # Output: 1000

# Try to set balance directly (not recommended)
# my_account.balance = -500  # This would raise an AttributeError

# Use the deposit and withdraw methods (which use the property's setter)
my_account.deposit(500)
my_account.withdraw(200)

# Try to withdraw more than the balance
my_account.withdraw(2000)
