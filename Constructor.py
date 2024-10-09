#Constructor

class Sdetails():
    '__init__ is inbulit constructor in python'
    'Self is just a pointer, instead of self we can use other names also'
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def getDetails(self):
        return(name,age,gender)


print("Constructor has been created succesfully ---- Class ~Sdetails")
