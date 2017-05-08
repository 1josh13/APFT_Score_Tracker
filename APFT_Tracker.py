import pickle
from os.path import expanduser
from metrics import pushup_groups_male
from metrics import pushup_groups_female
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
    def set_scores(self, pushup_reps, situp_reps, runtime, date):
        if self.gender == "Male":
            self.pushup_score = pushup_groups_male[self.age_group][pushup_reps]
            self.situp_score = situp_groups_unisex[self.age_group][situp_reps]
            keylist = []
            for key in run_groups_male[self.age_group].keys():
                keylist.append(key)
            while keylist.count(runtime) == 0:
                runtime = runtime + 1
            self.runtime_score = run_groups_male[self.age_group][runtime]
            total_score = self.pushup_score + self.situp_score + self.runtime_score
            self.scorelist.append((date, pushup_reps, self.pushup_score, situp_reps, self.situp_score, runtime, self.runtime_score, total_score))
        elif self.gender == "Female":
            self.pushup_score = pushup_groups_female[self.age_group][pushup_reps]
            self.situp_score = situp_groups_unisex[self.age_group][situp_reps]
            keylist = []
            for key in run_groups_male[self.age_group].keys():
                keylist.append(key)
            while keylist.count(runtime) == 0:
                runtime = runtime + 1
            #TODO: import female run standards, for now using male runtimes.
            self.runtime_score = run_groups_male[self.age_group][runtime]
            total_score = self.pushup_score + self.situp_score + self.runtime_score
            self.scorelist.append((date, pushup_reps, self.pushup_score, situp_reps, self.situp_score, runtime,
                                   self.runtime_score, total_score))
        else:
            print("Fatle Error, Can not set scores!")
    def print_scorelist(self):
        for entry in self.scorelist: # scorelist = [(str, int), (str, int), (str, int)]
            print('''
                Record Date: {}
                PU Reps: {} -- PU Score: {}
                SU Reps: {} -- SU Score: {}
                Runtime: {} -- Run Score: {}
                Total Score: {}'''.format(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))

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
        soldier_list = []
        return soldier_list

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
    1) Edit Selected Soldier Information
    2) View / Add / Edit APFT Scores
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
    '''.format(tmp.pushup_score, tmp.situp_score, tmp.runtime_score,
               tmp.pushup_score + tmp.situp_score + tmp.runtime_score))

def edit_gender():
    print("Select new gender:")
    print("1. Male")
    print("2. Female")
    soldiergenderstr = int(input("> "))
    if soldiergenderstr == 1:
        soldiergender = "Male"
    elif soldiergenderstr == 2:
        soldiergender = "Female"
    tmp.gender = soldiergender
    print("The soldiers gender has been changed!")

def edit_name():
    new_firstname = input("Enter new first name: ")
    new_lastname = input("Enter new last name: ")
    tmp.firstname = new_firstname
    tmp.lastname = new_lastname
    print("The soldiers name has been changed!")

soldier_list = loaddata(soldierdatafile)
while main_loop:
    print_main()
    main_choice = input("Enter Selection: ")
    if main_choice == "1":
        select_loop = True
        while select_loop:
            #Prints soldier list and asks for user choice.
            if not soldier_list:
                print("There are no soldier records to display!")
            else:
                print("You MUST select a soldier to edit before continuing!!!")
                for i in soldier_list:
                    print(soldier_list.index(i), i.get_name(), i.gender, i.age)
                soldier_select = int(input("Please enter your selection: "))
                tmp = soldier_list[soldier_select]
            print_select()
            select_choice = input("Enter Selection: ")
            #Enter "edit" mode to change selected soldiers attributes.
            if select_choice == "1":
                edit_loop_main = True
                while edit_loop_main:
                    print_edit()
                    edit_choice_info = input("Enter Selection: ")
                    if edit_choice_info == "1":
                        edit_name()
                    elif edit_choice_info == "2":
                        new_age = int(input("Enter new age: "))
                        tmp.age = new_age
                        print("The soldiers age has been changed!")
                    elif edit_choice_info == "3":
                        edit_gender()
                    elif edit_choice_info == "0":
                        print("Returning to selection menu!")
                        edit_loop_main = False
                    else:
                        print("You've entered an incorrect option {}!".format(edit_choice_info))
            #TODO: Add ability to edit records.
            elif select_choice == "2":
                edit_loop_apft = True
                while edit_loop_apft:
                    print_edit_apft()
                    apft_loop_choice = input("Enter Selection: ")
                    if apft_loop_choice == "1":
                        tmp.print_scorelist()
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