import os
import time

file_name = "Backup " + time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime()) + " .txt"
outfile = open(file_name, "w", encoding="utf8")
outfile.write("This back up was made on: " + time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime()))
separator = "\n" + "**" + "##"*30 + "**" + "\n"   #to seprate different scripts, trying to make it unique so it won't get mixed with the script's code

def lookin(path, main_dir):
    if main_dir:
        outfile.write(separator + path)    #saving the main directory of the backup and it will be used in the restore proccess

    dirlist = os.listdir(path)
    os.chdir(path)

    pyfileslist = list(filter(lambda x: x.endswith(".py"),dirlist))     #edit the lambda function to add other files types
    folderlist = list(filter(lambda x: "." not in x,dirlist))
    folderpathlist = list(map(lambda x: path + "\\" + x, folderlist))

    for py in pyfileslist:
        f = open(py, "r", encoding="utf8")
        try:
            outfile.write(separator + path + "\\" + py +separator + f.read())
        except:
            print("Error at " + path + "\\" + py)
    for folder in folderpathlist:
        try:
            lookin(folder, False)    #False becuase it's a sub directory and there is no need to save it separately
        except:
            pass   #not a folder but a file without extenstion

lookin(os.getcwd(), True)
outfile.close()