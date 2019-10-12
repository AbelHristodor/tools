import os
os.chdir(os.path.normpath(input("Enter a valid path: ")))
for i in range(10):
    with open("test"+str(i)+".mp3", "w+") as f:
        pass
    
    