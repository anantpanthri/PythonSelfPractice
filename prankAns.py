import os,re,sys
def rename_files():
    #(1) get files names from a folder
    file_list= os.listdir(r"C:\Users\ANANT PANTHRI\Downloads\prank\prank")
  # print(printfile)
    #(2) for each file, rename filename
    os.chdir(r"C:\Users\ANANT PANTHRI\Downloads\prank\prank")
    sp=os.getcwd()
    print(sp)
    newList=[]
    for names in file_list:
        newfile=re.sub("[0-9]","",names)
        os.rename(names, newfile)
        newList.append(newfile)
    os.chdir(sp)

rename_files()
   
