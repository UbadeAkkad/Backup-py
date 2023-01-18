import os

backupfile_name = "Backup 01-18-2023_15-05-54.txt"  #Backup file name
separator = "\n" + "**" + "##"*30 + "**" + "\n"      #Used separator in the backup file

backupfile = open(backupfile_name, "r", encoding="utf8")

backup_content = backupfile.read().split(separator)
main_dir = backup_content[1]
backup_content = backup_content[2:]   #to get rid of the backup create date and the main directory info

for i in range(0, len(backup_content), 2):
    path = backup_content[i].replace(main_dir,"").split("\\")  #to check for sub directory
    file_name = path[-1]
    if len(path) > 2:   #create sub directory if there is any
        try:
            os.makedirs(os.getcwd()+backup_content[i].replace(main_dir,"").replace(file_name,"").replace("\\","/"))
        except:
            pass  #folder already exsits
    writer = open("."+backup_content[i].replace(main_dir,""), "w", encoding="utf8")
    writer.write(backup_content[i+1])
    writer.close()
