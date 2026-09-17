class keyboard:
  def __init__(self,layout,brand,connectivity):
    self.layout = layout
    self.brand = brand
    self.connectivity = connectivity

  def typing(self):
    print("someone is typing")

  def illuminating(self):
    print(f"The keyboard has RGB lights")

  def connecting(self):
    print(f"The keyboard is connect")

  def describe(self):
    print(f"The keyboard layout is {self.layout}", f"The kayboard brand is {self.brand}",f"the kayboard connectivity is {self.connectivity}")

#self:se utiliza para decirle a python a que un objecto pertenece los atributos 
#create an instance using the class "keyboard"

keyboard1 = keyboard("QWERTY", "HP", "cable")
keyboard2 = keyboard("QWERTYÑ", "madcat", "bluethoot")

#we access to the object(instance) "keyboard1" to call its data 
print(keyboard1.layout)
print(keyboard2.brand)
keyboard1.typing()
keyboard2.describe()

#instance "keyboard2"

print(keyboard2.layout)



class BankAccount:
    def __init__(self,holder,balance):
        self.holder =holder
        self.__balance = balance

    def deposit(self,amout):
        if amount <= 0:
            print("The amount must be greather than 0")
        else:
            self.__balance += amount
            print(f"Successful transaction\n New balance: {self.__balance}")

    def withdraw(self,amount):
        if amount > __balance:
            print("insufficient funds")
        else:
            self.__balance -= amount
            print(f"Successful transaction\n New balance: {self.__balance}")
