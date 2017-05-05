from metrics import pushup_groups_male
from metrics import situp_groups_unisex
from metrics import run_groups_male
soldierList = []
main_loop = True
tmp = ""
#How to call score from dict:
#pushup_groups_male[26][5]
#TODO: Create load and save function in program.
class Soldier:
    def __init__(self, firstname, lastname, age, gender, age_group):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.age_group = age_group
        self.gender = gender
        self.scorelist = []
        self.pushup_score = 0
        self.situp_score = 0
        self.runtime_score = 0
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
    def get_pushup_score(self):
        return self.pushup_score
    def get_situp_score(self):
        return self.situp_score
    def get_runtime_score(self):
        return self.runtime_score
    def set_scores(self, pushup_reps, situp_reps, runtime, date):
        self.pushup_score = pushup_groups_male[self.age_group][pushup_reps]
        self.situp_score = situp_groups_unisex[self.age_group][situp_reps]
        keylist = []
        for key in run_groups_male[self.age_group].keys():
            keylist.append(key)
        while keylist.count(runtime) == 0:
            runtime = runtime + 1
        self.runtime_score = run_groups_male[self.age_group][runtime]
        self.scorelist.append((date, self.pushup_score + self.situp_score + self.runtime_score))
    def print_scorelist(self):
        for entry in self.scorelist: # scorelist = [(str, int), (str, int), (str, int)]
            print("Record Date: {} ------ Total Score: {}".format(entry[0], entry[1]))

def set_age_group(soldierage):
    if soldierage <= 21:
        return 21
    elif soldierage <= 26:
        return 26
    elif soldierage <= 31:
        return 31
    elif soldierage <= 36:
        return 36
    elif soldierage <= 41:
        return 41
    elif soldierage <= 46:
        return 46
    elif soldierage <= 51:
        return 51
    elif soldierage <= 56:
        return 56
    else:
        return False

while main_loop:
    print ('''
    Main Menu
    1) Edit Soldier Records
    2) View All Soldier Data
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
            2) Edit Selected Soldier Information
            3) View / Add / Edit APFT Scores
            0) Return to Main Menu
            ''')
            select_choice = input("Enter Selection: ")
            #Prints soldier list and asks for user choice.
            if select_choice == "1":
                if not soldierList:
                    print("There are no soldier records to display!")
                else:
                    for i in soldierList:
                        print(soldierList.index(i), i.get_name(), i.gender, i.age)
                    soldier_select = int(input("Please enter your selection: "))
                    tmp = soldierList[soldier_select]
            #Enter "edit" mode to change selected soldiers attributes.
            elif select_choice == "2":
                edit_loop_main = True
                while edit_loop_main:
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
                        print("Returning to selection menu!")
                        edit_loop_main = False
                    else:
                        print("You've entered an incorrect option {}!".format(edit_choice_info))
            #TODO
            elif select_choice == "3":
                edit_loop_apft = True
                while edit_loop_apft:
                    print('''
                    1) View APFT Scores
                    2) Add APFT Scores
                    3) Edit APFT Scores (Coming soon)
                    0) Return to Selection Menu
                    ''')
                    apft_loop_choice = input("Enter Selection: ")
                    #TODO: Add DATE --- SCORE style printout.
                    if apft_loop_choice == "1":
                        tmp.print_scorelist()
                        print('''
                        Pushups: {}
                        Situps: {}
                        2 Mile Run: {}
                        
                        Total Score: {} out of 300
                        '''.format(tmp.get_pushup_score(), tmp.get_situp_score(), tmp.get_runtime_score(), tmp.get_pushup_score() + tmp.get_situp_score() + tmp.get_runtime_score()))
                    elif apft_loop_choice == "2":
                        date = input("Enter the date of the record to input: MMDDYYY")
                        pushup_reps = int(input("Enter number of pushups preformed: "))
                        situp_reps = int(input("Enter number of situps preformed: "))
                        runtime = input("Enter 2 mile runtime MM:SS: ")
                        min, sec = runtime.split(':')
                        run_secs = int(min) * 60 + int(sec)
                        tmp.set_scores(pushup_reps, situp_reps, run_secs, date)
                        print('''
                        Pushups: {}
                        Situps: {}
                        2 Mile Run: {}

                        Total Score: {} out of 300
                        '''.format(tmp.get_pushup_score(), tmp.get_situp_score(), tmp.get_runtime_score(), tmp.get_pushup_score() + tmp.get_situp_score() + tmp.get_runtime_score()))
                    #TODO Edit apft scores.
                    #elif apft_loop_choice == "3":

                    elif apft_loop_choice == "0":
                        print("Returning to Selection Menu!")
                        edit_loop_apft = False
                    else:
                        print("You've entered an incorrect option: {}!".format(apft_loop_choice))
            elif select_choice == "0":
                print("Returning to main menu!")
                select_loop = False
            else:
                print("You've entered an incorrect option: {}!".format(select_choice))
    #Shows all soldier data.
    elif main_choice == "2":
        print("Showing all soldier data")
        for i in soldierList:
            print(soldierList.index(i), i.get_name(), i.gender, i.age)
    #Imputs new soldier data into soldier class as an object of the class.
    elif main_choice == "3":
        firstname = input("Enter Soldier's first name: ")
        surname = input("Enter Soldier's last name: ")
        soldierage = int(input("Enter Soldier's Age: "))
        print("Select Soldier's Gender:")
        print("1. Male")
        print("2. Female")
        soldiergenderstr = int(input("> "))
        if soldiergenderstr == 1:
            soldiergender = "Male"
        elif soldiergenderstr == 2:
            soldiergender = "Female"
        else:
            print("You dun fucked up")
        soldier_age_group = set_age_group(soldierage)
        soldierList.append(Soldier(firstname, surname, soldierage, soldiergender, soldier_age_group))
        print("Soldier, {} {}, age {} {} added to the database!".format(firstname, surname, soldierage, soldiergender))
    #Exits the program.
    elif main_choice == "0":
        print("Goodbye!")
        main_loop = False
    else:
        print("You've entered a incorrect option: {}!".format(main_choice))