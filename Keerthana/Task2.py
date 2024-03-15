import os
file_name=input("enter the name")
directory="C:\\Users\\kisho\\OneDrive\\Desktop\\Tasks"
print(os.getcwd())
file_list=os.listdir(directory)
print(file_list)
print("files created:")
if file_name in file_list:
    print(f"{file_name}: This is the file")
else:
    print("no file")
    
