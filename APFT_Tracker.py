from metrics import pushup_groups_male
soldierList = []
main_loop = True
tmp = ""
#How to call score from dict:
#pushup_groups_male[26][5]
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
    1) Edit Soldier Records
    2) View All Records
    3) Add a Soldier
    0) Exit Program
    ''')
    main_choice = input("Enter Selection: ")
    if main_choice == "1":
        select_loop = True
        while select_loop:
            print('''
            Selection Menu
            1) Select Soldier
            2) Edit Selected Soldier Records
            0) Return to Main Menu
            ''')
            select_choice = input("Enter Selection: ")
            if select_choice == "1":
                if not soldierList:
                    print("There are no soldier records to display!")
                else:
                    for i in soldierList:
                        print(soldierList.index(i), i.get_name(), i.gender, i.age)
                    soldier_select = int(input("Please enter your selection: "))
                    tmp = soldierList[soldier_select]
            elif select_choice == "2":
                edit_loop_main = True
                while edit_loop_main:
                    print('''
                    1) Edit Soldier Name, Age, Gender.
                    2) Edit Soldier APFT Data.
                    0) Return
                    ''')
                    edit_choice_main = input("Enter Selection: ")
                    if edit_choice_main == "1":
                        edit_loop_info = True
                        while edit_loop_info:
                            print('''
                            1) Edit Soldier Name.
                            2) Edit Soldier Age.
                            3) Edit Solder Gender.
                            0) Return
                            ''')
                            edit_choice_info = input("Enter Selection: ")
                            if edit_choice_info == "1":
                                new_firstname = input("Enter new first name: ")
                                new_lastname = input("Enter new last name: ")
                                tmp.set_name(new_firstname, new_lastname)
                                print("The soldiers name has been changed!")
                            elif edit_choice_info == "2":
                                new_age = int(input("Enter new age: "))
                                tmp.set_age(new_age)
                                print("The soldiers age has been changed!")
                            elif edit_choice_info == "3":
                                new_gender = input("Enter the new gender: ")
                                tmp.set_gender(new_gender)
                                print("The soldiers gender has been changed!")
                            elif edit_choice_info == "0":
                                print("Returning to edit selection menu!")
                                edit_loop_info = False
                            else:
                                print("You've entered an incorrect option {}!".format(edit_choice_info))
                    elif edit_choice_main == "2":
                        edit_loop_apft = True
                        #while edit_loop_apft:
                        #Need to design and implement APFT standards / charts.
                    elif edit_choice_main == "0":
                        print("Returning to selection menu!")
                        edit_loop_main = False
                    else:
                        print("You've entered an incorrect option {}!".format(edit_choice_main))
            elif select_choice == "0":
                print("Returning to main menu!")
                select_loop = False
            else:
                print("You've entered an incorrect option {}!".format(select_choice))
    elif main_choice == "2":
        print("Showing all records")
        for i in soldierList:
            print(soldierList.index(i), i.get_name(), i.gender, i.age)
    elif main_choice == "3":
        firstname = input("Enter Soldier's first name: ")
        surname = input("Enter Soldier's last name: ")
        soldierage = input("Enter Soldier's Age: ")
        soldiergender = input("Enter Soldier's Gender: ")
        soldierList.append(Soldier(firstname, surname, soldierage, soldiergender))
        print("Soldier, {} {}, age {} {} added to the database!".format(firstname, surname, soldierage, soldiergender))
    elif main_choice == "0":
        print("Goodbye!")
        main_loop = False
    else:
        print("You've entered a incorrect option {}!".format(main_choice))