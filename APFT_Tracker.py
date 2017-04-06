soldierList = []
looping = True

class Soldier:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
    def get_name(self):
        return self.firstname + " " + self.lastname
    def set_name(self, firstname, lastname):
        if self.firstname != firstname:
            self.firstname = firstname
        if self.lastname != lastname:
            self.lastname = lastname
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def get_gender(self):
        return self.gender
    def set_gender(self, gender):
        self.gender = gender

while looping:
    print (''' 
    Main Menu
    1) Select Soldier
    2) View All Records
    3) Add a Soldier
    0) Exit Program
    ''')
    choice = input("Enter Selection> ")
    if choice == "1":
        if not soldierList:
            print("There are no soldier records to display!")
        else:
            for i in soldierList:
                print(i.get_name(), i.gender, i.age)

    elif choice == "2":
        print("Showing all records")
    elif choice == "3":
        firstname = input("Enter Soldier's first name: ")
        surname = input("Enter Soldier's last name: ")
        soldierage = input("Enter Soldier's Age: ")
        soldiergender = input("Enter Soldier's Gender: ")
        soldierList.append(Soldier(firstname, surname, soldierage, soldiergender))
        print("Solder, {} {}, age {} {} added to the database!".format(firstname, surname, soldierage, soldiergender))
    elif choice == "0":
        print("Goodbye!")
        looping = False
    else:
        print("You've entered a incorrect option {}!".format(choice))
