#Inheritance

class User():
    def __init__(self, email):
        self.email  = email

    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self, name, power, email):
         # Calling init method of SUper class
        #User.__init__(self,email) 
        super().__init__(email) #other way of calling init method
       
        self.name = name
        self.power =power

    def attack(self):
        print(f'Attacking with poiwer of {self.power}')

class Archer(User):
    def __init__(self, name , num_arrows):
        self.name = name
        self.num_arrows =  num_arrows

    def attack(self):
        print(f'Attacking with poiwer of {self.num_arrows}')


# Introspection

wizard1= Wizard("Ashish" , 50, "ashishdeshpande91@gmail.com")
archer1= Archer("Sachin", 100)
wizard1.attack()
print(dir(wizard1))
 


