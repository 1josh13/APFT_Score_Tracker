import pickle
from os.path import expanduser
from metrics import pushup_groups_male
from metrics import situp_groups_unisex
from metrics import run_groups_male
homepath = expanduser("~\\Documents\\")
soldierdatafile = homepath+"soldierdata.txt"
main_loop = True
tmp = ""
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
#TODO: Remove lines 31-44 and check rest of code for issues.
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

def loaddata(filename):
    try:
        with open(soldierdatafile, 'rb') as input:
            print(input)
            soldier_list = pickle.load(input)
            return soldier_list
    except:
        print("No Data in file.")
def savedata(filename):
    with open(soldierdatafile, 'wb+') as output:
        pickle.dump(soldier_list, output, pickle.HIGHEST_PROTOCOL)

def print_main():
    print ('''
    Main Menu
    1) Edit Soldier Records
    2) View All Soldier Data
    3) Add a Soldier
    0) Exit's Program and Saves Data
    ''')

def print_select():
    print('''
    Selection Menu
    1) Select Soldier
    2) Edit Selected Soldier Information
    3) View / Add / Edit APFT Scores
    0) Return to Main Menu
    ''')

def print_edit():
    print('''
    1) Edit Soldier's Name.
    2) Edit Soldier's Age.
    3) Edit Soldier's Gender.
    0) Return
    ''')

def print_edit_apft():
    print('''
    1) View APFT Scores
    2) Add APFT Scores
    3) Edit APFT Scores (Coming soon)
    0) Return to Selection Menu
    ''')

def print_apft_list():
    tmp.print_scorelist()
    print('''
    Pushups: {}
    Situps: {}
    2 Mile Run: {}

    Total Score: {} out of 300
    '''.format(tmp.get_pushup_score(), tmp.get_situp_score(), tmp.get_runtime_score(), tmp.get_pushup_score() + tmp.get_situp_score() + tmp.get_runtime_score()))

def print_all_soldiers():
    print("Showing all soldier data")
    for i in soldier_list:
        print(soldier_list.index(i), i.get_name(), i.gender, i.age)

def add_soldier():
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
    soldier_list.append(Soldier(firstname, surname, soldierage, soldiergender, soldier_age_group))
    print("Soldier, {} {}, age {} {} added to the database!".format(firstname, surname, soldierage, soldiergender))

def add_new_apft():
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
    '''.format(tmp.get_pushup_score(), tmp.get_situp_score(), tmp.get_runtime_score(),
               tmp.get_pushup_score() + tmp.get_situp_score() + tmp.get_runtime_score()))

soldier_list = loaddata(soldierdatafile)
while main_loop:
    print_main()
    main_choice = input("Enter Selection: ")
    if main_choice == "1":
        select_loop = True
        while select_loop:
            print_select()
            select_choice = input("Enter Selection: ")
            #Prints soldier list and asks for user choice.
            if select_choice == "1":
                if not soldier_list:
                    print("There are no soldier records to display!")
                else:
                    for i in soldier_list:
                        print(soldier_list.index(i), i.get_name(), i.gender, i.age)
                    soldier_select = int(input("Please enter your selection: "))
                    tmp = soldier_list[soldier_select]
            #Enter "edit" mode to change selected soldiers attributes.
            elif select_choice == "2":
                edit_loop_main = True
                while edit_loop_main:
                    print_edit()
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
            #TODO: Add ability to edit records.
            elif select_choice == "3":
                edit_loop_apft = True
                while edit_loop_apft:
                    print_edit_apft()
                    apft_loop_choice = input("Enter Selection: ")
                    if apft_loop_choice == "1":
                        print_apft_list()
                    elif apft_loop_choice == "2":
                        add_new_apft()
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
        print_all_soldiers()
    #Imputs new soldier data into soldier class as an object of the class.
    elif main_choice == "3":
        add_soldier()
    #Exits the program.
    elif main_choice == "0":
        print("Goodbye!")
        savedata(soldierdatafile)
        main_loop = False
    else:
        print("You've entered a incorrect option: {}!".format(main_choice))