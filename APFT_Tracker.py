soldierList = []
main_loop = True
selected_soldier = ""
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

while main_loop:
    print (''' 
    Main Menu
    1) Soldier Selection
    2) View All Records
    3) Add a Soldier
    0) Exit Program
    ''')
    choice = input("Enter Selection> ")
    if choice == "1":
        select_loop = True
        while select_loop:
            print('''
            Selection Menu
            1) Select Soldier
            2) Edit Selected Soldier Records
            0) Return to Main Menu
            ''')
            select_choice = input("Enter Selection> ")
            if select_choice == "1":
                if not soldierList:
                    print("There are no soldier records to display!")
                else:
                    for i in soldierList:
                        print(soldierList.index(i), i.get_name(), i.gender, i.age)
                    soldier_select = input("Please enter your selection: ")
            elif select_choice == "2":
                edit_loop = True
                while edit_loop:

                    print('''
                    1) Edit Soldier Name, Age, Gender
                    2) Edit Soldier APFT Data
                    0) Return
                    ''')
                    edit_choice = input("Enter Selection: ")
                    if edit_choice == "1":

                    elif edit_choice == "2":

                    elif edit_choice == "0":
                        print("Returning to selection menu!")
                        edit_loop = False

            elif select_choice == "0":
                print("Returning to main menu!")
                select_loop = False
            else:
                print("You've entered an incorrect option {}!".format(select_choice))
    elif choice == "2":
        print("Showing all records")
        for i in soldierList:
            print(soldierList.index(i), i.get_name(), i.gender, i.age)
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
