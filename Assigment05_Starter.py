# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# James Henderson, 8.10.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
file_str = "ToDoList.txt"  # An object that represents a file
file_obj = None  # initialize an object for the text file
data_str = ""  # A row of text data from the file
row_lst = []  # A list made up of one row of text data from the file
row_dict = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
MENU_STR = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """  # A menu of user options
choice_str = ""  # A String variable to capture the user's option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    file_obj = open(file_str, 'r')

    for data_str in file_obj:
        row_lst = data_str.split(',')  # Returns a list!
        row_dict = {'Task': row_lst[0], 'Priority': row_lst[1].strip()}
        table_lst.append(row_dict)

    file_obj.close()

except FileNotFoundError:
    pass

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

# def show_list():
#     print("Here are the current tasks:")
#     print("Task\t|\tPriority\n"
#           "-------------------------------")
#     for row in table_lst:
#         print(row['Task'] + '\t|\t' + row['Priority'])


while True:
    print(MENU_STR)
    choice_str = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if choice_str.strip() == '1':
        # show_list()
        print("Here are the current tasks:")
        print("Task\t|\tPriority\n"
              "-------------------------------")
        for row in table_lst:
            print(row['Task'] + '\t|\t' + row['Priority'])

    # Step 4 - Add a new item to the list/Table
    elif choice_str.strip() == '2':
        task_str = input("Please enter a task: ").capitalize()
        priority_str = input("Please enter a priority: ").capitalize()

        task_dict = {'Task': task_str, 'Priority': priority_str}
        table_lst.append(task_dict)
        print("Item added.")
        # show_list()
        print("Here are the current tasks:")
        print("Task\t|\tPriority\n"
              "-------------------------------")
        for row in table_lst:
            print(row['Task'] + '\t|\t' + row['Priority'])

    # Step 5 - Remove an item from the list/Table
    elif choice_str.strip() == '3':
        # show_list()
        print("Here are the current tasks:")
        print("Task\t|\tPriority\n"
              "-------------------------------")
        for row in table_lst:
            print(row['Task'] + '\t|\t' + row['Priority'])
        remove_str = input('\nWhich task would you like to delete? ')

        taskfound_bln = False
        for task_dict in table_lst:
            if task_dict['Task'].lower() == remove_str.lower():
                table_lst.remove(task_dict)
                taskfound_bln = True
                print("Task deleted.")

        if not taskfound_bln:
            print("Sorry, that task is not in the list. No tasks were removed.")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif choice_str.strip() == '4':
        file_obj = open(file_str, 'w')
        for task_dict in table_lst:
            file_obj.write(task_dict['Task'] + ',' + task_dict['Priority'] + '\n')

        file_obj.close()
        print("Data successfully saved.")

    # Step 7 - Exit program
    elif choice_str.strip() == '5':
        print("Goodbye!")
        break  # and Exit the program

    else:
        print("Please enter a valid choice [1-5].")
