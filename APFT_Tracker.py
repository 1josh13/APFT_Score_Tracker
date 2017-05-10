import pickle
from os.path import expanduser
from metrics import pushup_groups_male
from metrics import pushup_groups_female
from metrics import situp_groups_unisex
from metrics import run_groups_male
from metrics import run_groups_female
homepath = expanduser("~\\Documents\\")
soldierdatafile = homepath+"soldierdata.txt"
main_loop = True
tmp = ""
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
    # Converts entered rep's and time to scores. Stores in scorelist for each soldier.
    def set_scores(self, pushup_reps, situp_reps, runtime, date):
        if self.gender == "Male":
            if pushup_reps >= 77:
                pushup_reps = 77
            if situp_reps >= 82:
                situp_reps = 82
            if runtime <= 780:
                runtime = 780
            self.pushup_score = pushup_groups_male[self.age_group][pushup_reps]
            self.situp_score = situp_groups_unisex[self.age_group][situp_reps]
            keylist = []
            for key in run_groups_male[self.age_group].keys():
                keylist.append(key)
            while keylist.count(runtime) == 0:
                runtime = runtime + 1
            self.runtime_score = run_groups_male[self.age_group][runtime]
            total_score = self.pushup_score + self.situp_score + self.runtime_score
            self.scorelist.append([date, pushup_reps, self.pushup_score, situp_reps, self.situp_score, runtime, self.runtime_score, total_score])
        elif self.gender == "Female":
            if pushup_reps >= 51:
                pushup_reps = 51
            if situp_reps >= 82:
                situp_reps = 82
            if runtime <= 930:
                runtime = 930
            self.pushup_score = pushup_groups_female[self.age_group][pushup_reps]
            self.situp_score = situp_groups_unisex[self.age_group][situp_reps]
            keylist = []
            for key in run_groups_female[self.age_group].keys():
                keylist.append(key)
            while keylist.count(runtime) == 0:
                runtime = runtime + 1
            self.runtime_score = run_groups_female[self.age_group][runtime]
            total_score = self.pushup_score + self.situp_score + self.runtime_score
            self.scorelist.append([date, pushup_reps, self.pushup_score, situp_reps, self.situp_score, runtime, self.runtime_score, total_score])
        else:                       #0          1               2           3               4           5           6                   7
            print("Fatal Error, Can not set scores!")
    def edit_score_pushups(self, new_pushup_reps, listselect):
        if self.gender == "Male":
            if new_pushup_reps >= 77:
                new_pushup_reps = 77
            self.pushup_score = pushup_groups_male[self.age_group][new_pushup_reps]
            self.scorelist[listselect][1] = new_pushup_reps
            self.scorelist[listselect][2] = self.pushup_score
            print("Pushups have been modified!")
        elif self.gender == "Female":
            if new_pushup_reps >= 51:
                new_pushup_reps = 51
            self.pushup_score = pushup_groups_female[self.age_group][new_pushup_reps]
            self.scorelist[listselect][1] = new_pushup_reps
            self.scorelist[listselect][2] = self.pushup_score
            print("Pushups have been modified!")
        total_score = self.pushup_score + self.situp_score + self.runtime_score
        self.scorelist[listselect][7] = total_score
    def edit_score_situps(self, new_situp_reps, listselect):
        if self.gender == "Male":
            if new_situp_reps >= 82:
                new_situp_reps = 82
            self.pushup_score = situp_groups_unisex[self.age_group][new_situp_reps]
            self.scorelist[listselect][3] = new_situp_reps
            self.scorelist[listselect][4] = self.situp_score
            print("Situps have been modified!")
        elif self.gender == "Female":
            if new_situp_reps >= 82:
                new_situp_reps = 82
            self.situp_score = situp_groups_unisex[self.age_group][new_situp_reps]
            self.scorelist[listselect][3] = new_situp_reps
            self.scorelist[listselect][4] = self.situp_score
            print("Situps have been modified!")
        total_score = self.pushup_score + self.situp_score + self.runtime_score
        self.scorelist[listselect][7] = total_score
    def edit_score_run(self, new_run_time, listselect):
        min, sec = new_run_time.split(':')
        new_run_time = int(min) * 60 + int(sec)
        if self.gender == "Male":
            if new_run_time <= 780:
                new_run_time = 780
            keylist = []
            for key in run_groups_male[self.age_group].keys():
                keylist.append(key)
            while keylist.count(new_run_time) == 0:
                new_run_time = new_run_time + 1
            self.runtime_score = run_groups_male[self.age_group][new_run_time]
            self.scorelist[listselect][5] = new_run_time
            self.scorelist[listselect][6] = self.runtime_score
            print("Runtime has been modified!")
        elif self.gender == "Female":
            if new_run_time <= 930:
                new_run_time = 930
            keylist = []
            for key in run_groups_female[self.age_group].keys():
                keylist.append(key)
            while keylist.count(new_run_time) == 0:
                new_run_time = new_run_time + 1
            self.pushup_score = run_groups_female[self.age_group][new_run_time]
            self.scorelist[listselect][5] = new_run_time
            self.scorelist[listselect][6] = self.runtime_score
            print("Runtime has been modified!")
        total_score = self.pushup_score + self.situp_score + self.runtime_score
        self.scorelist[listselect][7] = total_score
    def print_scorelist(self):
        for entry in self.scorelist: # scorelist = [(str, int), (str, int), (str, int)]
            print('''
                Record Date: {}
                PU Reps: {} -- PU Score: {}
                SU Reps: {} -- SU Score: {}
                Runtime: {} -- Run Score: {}
                Total Score: {}'''.format(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))

# Sets soldier age group based on inputted age.
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

# Loads saved data, if no data in file, returns an empty list.
def loaddata(filename):
    try:
        with open(soldierdatafile, 'rb') as input:
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

# Creates a new soldier object and appends to soldier_list.
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

# Adds new APFT record to selected soldier.
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

# Edit's soldier gender.
def edit_gender():
    print("Select new gender:")
    print("1. Male")
    print("2. Female")
    soldiergenderstr = int(input("> "))
    if soldiergenderstr == 1:
        soldiergender = "Male"
    elif soldiergenderstr == 2:
        soldiergender = "Female"
    else:
        print("You've entered an incorrect choice! {}".format(soldiergenderstr))
    tmp.gender = soldiergender
    print("The soldiers gender has been changed!")

# Edits soldier name.
def edit_name():
    new_firstname = input("Enter new first name: ")
    new_lastname = input("Enter new last name: ")
    tmp.firstname = new_firstname
    tmp.lastname = new_lastname
    print("The soldiers name has been changed!")

# Edits apft record entires in selected soldier records.
def edit_apft():
    for entry in tmp.scorelist:  # scorelist = [(str, int), (str, int), (str, int)]
        print('''
            Record # {}
            Record Date: {}
            PU Reps: {} -- PU Score: {}
            SU Reps: {} -- SU Score: {}
            Runtime: {} -- Run Score: {}
            Total Score: {}'''.format(tmp.scorelist.index(entry)+1, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))
    edit_apft_listselect = int(input("Select the Record number to edit (-1 to quit): "))
    if edit_apft_listselect == -1:
        return
    else:
        edit_apft_listselect = edit_apft_listselect - 1
        print('''
        What score would you like to edit?
        1) Pushups
        2) Situps
        3) Run
        ''')
        edit_apft_scoreselect = int(input("Enter Selection (-1 to quit): "))
        if edit_apft_scoreselect == -1:
            return
        elif edit_apft_scoreselect == 1:
            new_pushup_reps = int(input("Please enter the correct number of Pushup Repetitions that the soldier performed: "))
            tmp.edit_score_pushups(new_pushup_reps, edit_apft_listselect)
        elif edit_apft_scoreselect == 2:
            new_situp_reps = int(input("Please enter the correct number of Situp Repetitions that the soldier performed: "))
            tmp.edit_score_situps(new_situp_reps, edit_apft_listselect)
        elif edit_apft_scoreselect == 3:
            new_runtime = input("Please enter the correct runtime of the soldier MM:SS: ")
            tmp.edit_score_run(new_runtime, edit_apft_listselect)
        else:
            print("You've entered an incorrect option!")

# Edits soldier age.
def edit_age():
    new_age = int(input("Enter soldiers new age: "))
    tmp.age = new_age
    print("The soldiers age has been changed!")

def force_soldier_select():
    global tmp
    if not soldier_list:
        print("There are no soldier records to display!")
    else:
        print("You MUST select a soldier to edit before continuing!!!")
        print_all_soldiers()
        soldier_select = int(input("Please enter your selection (Type -1 to quit):  "))
        if soldier_select == -1:
            select_loop = False
            return select_loop
        elif soldier_select <= len(soldier_list):
            tmp = soldier_list[soldier_select]
            return tmp
        else:
            print("It appears you've entered an incorrect selection.")

# Calls function to load saved data.
soldier_list = loaddata(soldierdatafile)
# Start of main function
while main_loop:
    print_main()
    main_choice = input("Enter Selection: ")
    if main_choice == "1":
        select_loop = True
        while select_loop:
            # Prints soldier list and asks for user choice.
            if not force_soldier_select():
                break
            print_select()
            select_choice = input("Enter Selection: ")
            # Enter "edit" mode to change selected soldiers attributes.
            if select_choice == "1":
                edit_loop_main = True
                while edit_loop_main:
                    print_edit()
                    edit_choice_info = input("Enter Selection: ")
                    if edit_choice_info == "1":
                        edit_name()
                    elif edit_choice_info == "2":
                        edit_age()
                    elif edit_choice_info == "3":
                        edit_gender()
                    elif edit_choice_info == "0":
                        print("Returning to selection menu!")
                        edit_loop_main = False
                    else:
                        print("You've entered an incorrect option {}!".format(edit_choice_info))
            elif select_choice == "2":
                edit_loop_apft = True
                while edit_loop_apft:
                    print_edit_apft()
                    apft_loop_choice = input("Enter Selection: ")
                    if apft_loop_choice == "1":
                        tmp.print_scorelist()
                    elif apft_loop_choice == "2":
                        add_new_apft()
                    elif apft_loop_choice == "3":
                        edit_apft()
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