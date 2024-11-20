# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Katherine Sather, 11/17/2024, Updated the Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the script variables.
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# I have commented out the rest of the variables as we'll no longer need them:
#student_first_name: str = ''  # Holds the first name of a student entered by the user.
#student_last_name: str = ''  # Holds the last name of a student entered by the user.
#course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: dict = {}  # one row of student data
#csv_data: str = ''  # Holds combined string data separated by a comma.
#json_data: str = ''  # Holds combined string data in a json format.
#file = None  # Holds a reference to an opened file.


# Processing--------------------------------------- # adding this section title per SOC
class FileProcessor:
    """
    This is a collection of processing functions for working with a JSON file.
    ChangeLog: (Who, When, What)
    KSather, 11/16/2024,Created Class
    KSather, 11/18/2024, Added read function
    KSather, 11/18/2024, Adding write function
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads student data from a JSON file and loads it into a list.
        ChangeLog: (Who, When, What)
        KSather, 11/16/2024,Created function
        :return: list
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function will write data to the JSON file
        ChangeLog: (Who, When, What)
        Katherine Sather, 11/18/2024, Created function
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file. \n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()

# Presentation--------------------------------------- # Adding this section title per SOC
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    KSather, 11/16/2024,Created Class
    KSather 11/18/2024, Added error message function
    KSather, 11/18,2024, Added output menu function
    KSather, 11/18/2024, Added input menu choice function
    Ksather 11/19/2024, Added output student courses function
    Ksather 11/19/2024, Added input student data function
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        KSather, 11/18/2024, Created function
        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        KSather, 11/18/2024,Created function
        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
        ChangeLog: (Who, When, What)
        KSather, 11/18/2024,Created function
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the students and course names to the user.

        ChangeLog: (Who, When, What)
        KSather, 11/18/2024, Created function
        :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name for each user
        ChangeLog: (Who, When, What)
        KSather, 11/18/2024, Created function
        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values isn't the correct data type.", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data

#Beginning of the main body----------------------------------------------------------------------------------------------

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present the menu of choices
while (True):
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        except Exception as e:
            IO.output_error_messages(message="An error occurred while saving data.", error=e)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
