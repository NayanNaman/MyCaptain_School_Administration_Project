#import

import csv

#defining a function

def convert_csv(info_list):
    with open("Student_info.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact No.", "E-Mail ID"])
        writer.writerow(info_list)

#inputs
        
if __name__ == '__main__':
    condition = True
    student_no = 1
    while condition == True: 
        student_info=input("\nPlease enter student #{} information in the following format (Name [Sapce] Age [Space] Contact_No. [Space] E-Mail_ID): ".format(student_no))
        split_info = student_info.split(" ")
        print("\nYou entered the following information:\nName: {}\nAge: {}\nContact_No.: {}\nE-Mail ID: {}"
              .format(split_info[0], split_info[1], split_info[2], split_info[3]))

#verifying the inputs
        
        choice_loop = True
        choice = input("Do you want to change it? (yes/no): ")
        while choice_loop == True:
            if choice.lower() == "no":
                print ("Your inputs have been saved.")
                choice_loop = False

                convert_csv(split_info)

                #reentering inputs
                check_loop = True
                while check_loop == True:
                    check = input("\nDo you want to enter another student's information? (yes/no): ")
                    if check.lower() == "yes":
                        student_no = student_no + 1
                        condition = True
                        check_loop = False
                    elif check.lower() == "no":
                        print ("\nThanks for using this. Your file has been created.")
                        condition = False
                        check_loop = False
                    else:
                        print("Please enter only 'yes' or 'no' as input!!")
                        condition = True
                        check_loop = True

            elif choice.lower() == "yes":
                print("\nPlease re-enter the information.")
                choice_loop = False
            else:
                print("Please enter only 'yes' or 'no' as input!!")
                choice_loop = False
