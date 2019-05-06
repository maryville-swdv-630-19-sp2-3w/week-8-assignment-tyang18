class PreBuilt:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
        self.topping0 = "cheese"
        
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getSize(self):
        return self.size
    
    def getTopping0(self):
        return self.topping0
    
class Hawaiian(PreBuilt):
    def __init__(self, topping1="Ham", topping2="Pineapple"):
        PreBuilt.__init__(self, name, price, size)
        self.topping1 = topping1
        self.topping2 = topping2
        
    def getTopping1(self):
        return self.topping1
    
    def getTopping2(self):
        return self.topping2
    
class Sausage(PreBuilt):
    def __init__(self, topping1="Sausage"):
        PreBuilt.__init__(self, name, price, size)
        self.topping1 = topping1
        
    def getTopping1(self):
        return self.topping1
    
class Drinks:
    def __init__(self, size, options):
        self.size = size
        self.options = options
        
    def getSize(self):
        return self.size
    
    def getOptions(self):
        return self.getOptions

    
class Custom:
    def __init__(self, size, topping1, topping2, topping3):
        self.size = size
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3
        self.price = price
        self.finalBuild = []
        
    def getSize(self):
        return self.size
    
    def getTopping1(self):
        return self.topping1
    
    def getTopping2(self):
        return self.topping2
    
    def getTopping3(self):
        return self.topping3
    
    def getFinalBuild(self):
        self.finalBuild = self.finalBuild.append(topping1)
        self.finalBuild = self.finalBuild.append(topping2)
        self.finalBuild = self.finalBuild.append(topping3)
        
class SignUp:
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        
    def getUser(self):
        return self.userName
    
    def getPass(self):
        return self.passWord
    
    def generateProfile(self):
        print("Your account {} has been created.")
        