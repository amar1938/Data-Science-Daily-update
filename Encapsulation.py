#ENCAPSULATION
'Creating a Public class'

class mobile():
    def __init__(self,Modle,year):
        self.model = Modle
        self.year = year
print("Public Class Created Successfully")

model = input("Enter Mobile Model:")
year = int(input("Enter Mobile Year:"))
m = mobile(model,year)

'Creating Private Class'

print("\n Private Class Created Successfully")
class Car():
    def __init__(self,model,year):
        " ' __' before variable makes the variable private to class"
        self.__model = model
        self.__year = year

m1 = input("Enter Car model:")
y = int(input("Enter Car YEar:"))
c = Car(m1,y)
