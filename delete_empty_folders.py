"""
@author: Abel Hristodor 
@projectName: Delete Empty Folders
@description: Deletes all empty folder in a given dir.
@github: https://github.com/AbelHristodor

"""
import os, time

def main():

    print('''
    ------- CREDITS -------\n
    @author: Abel Hristodor 
    @projectName: Delete Empty Folders
    @description: Deletes all empty folder in a given dir.
    @github: https://github.com/AbelHristodor
    \n
    ''')


    while True:
        try:
            raw_path = input(" Please enter the path to the folder to clean: ")
            os.chdir(raw_path)
            path = os.getcwd()
            print(f"\nDirectory: {path}")
            break
        except:
            print("\n ERROR: --- Please enter a valid path ---")
            continue
    
    print("\nWould you like me to do a deep scan? aka also into subfolders? Y/N")
    answer = input()

    if answer.lower == "y" or answer.lower == 'yes':
        deep_scan = True
    else: 
        deep_scan = False

    time.sleep(0.2)

    if deep_scan:
        deep_scan_and_delete(path)
    else:
        simple_scan_and_delete(path)
    
    print("Job Completed.")
    return
    

def deep_scan_and_delete(path):
    for root, subdirs, files in os.walk(path):
        for subdir in subdirs:
            dir_path = root + "\\" + subdir
            try:
                os.rmdir(dir_path)
            except (FileNotFoundError, OSError) as e:
                print(f"Found dir: '{subdir}' contains with files, skipping...")
                time.sleep(0.3)
            else:
                print(f"Folder: {subdir} successfully deleted.")
    return

def simple_scan_and_delete(path):
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                try:
                    os.rmdir(entry.path)
            except (FileNotFoundError, OSError) as e:
                print(f"Found dir: '{entry.name}' contains with files, skipping...")
                time.sleep(0.3)
            else:
                print(f"Folder: {entry.name} successfully deleted.")
    return



if __name__ == "__main__":
    main()
