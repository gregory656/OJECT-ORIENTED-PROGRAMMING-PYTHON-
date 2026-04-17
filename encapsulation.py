class BankAccount:
    def__init__(self,owner,balance=0):        """
        Initialize a new BankAccount instance.
        :param owner: The name of the account holder.
        :param balance: Initial balance, defaults to 0.
        """
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")        if not owner:
            raise ValueError("Owner name cannot be empty.")

        self.owner = owner
        self.__balance = balance #private attribute
        #self.__balance is Encapsulated, it can only be accessed within the class
        #double underscore is used to indicate that the attribute is private(name mangling)


    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficent funds")
        else:
            self.__balance -= amount

            #deposit and withdraw are methods Ie for controlled acces not allowing random modification


    def get_balance(self):
        return self.__balance