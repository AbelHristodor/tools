"""
@author: Abel Hristodor 
@projectName: AutoRenamer
@description: Renames all files in a given folder
@github: https://github.com/AbelHristodor
 
"""
import os, time

def main():
    print('''
    ------- CREDITS -------\n
    @author: Abel Hristodor 
    @projectName: AutoRenamer
    @description: Renames all files in a given folder
    @github: https://github.com/AbelHristodor\n
    ''')

    print(" ------- Folder Selection -------")
    while True:
        try:
            curr_working_dir = os.chdir(os.path.normpath(input(" Please enter the path to the folder containing the files you want to rename: ")))
            break
        except:
            print("\n ERROR: --- Please enter a valid path ---")
            continue


    file_number = 1
    print("\n ------- Data -------\n")
    file_title = input(" New file name: ")
    extension = input(" New extension / same extension: ")

    format_choices = {
        "Number_Filename.extension" : f"{file_number}_{file_title}.{extension}",
        "Filename_Number.extension" : f"{file_title}_{file_number}.{extension}",
        "FilenameNumber.extension" : f"{file_title}{file_number}.{extension}",
    }
    
    
    # File handling
    
    format_choice = list(format_choices.keys())[selectFormat(format_choices)-1]
    with os.scandir(curr_working_dir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                format_choices = {
                    "Number_Filename.extension" : f"{file_number}_{file_title}.{extension}",
                    "Filename_Number.extension" : f"{file_title}_{file_number}.{extension}",
                    "FilenameNumber.extension" : f"{file_title}{file_number}.{extension}",
                }
                dest = format_choices[format_choice]
                os.rename(entry.name, dest)
                file_number += 1 
        print("\n SUCCESS: --- All files have been successfully renamed ---")
        time.sleep(2)

 #C:\Users\habel\Desktop\test
# 
def selectFormat(format_choices):
    print("Please select a format\n")
    c = 0
    for k,v in format_choices.items():
        print(f"{c+1}: {k} -> {v}")
        c+=1

    while(True):
        try:
            choice = int(input("Choice: "))
            if choice > len(format_choices) or choice < 1:
                print("\n ERROR: --- Please enter a valid number ---")
                continue
            else: 
                return choice
        except TypeError :
            print("\n ERROR: --- Please enter a valid number ---")
            continue



if __name__ == "__main__":
    main()