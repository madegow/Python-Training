'''
import os

def get_file_owner(file_path):
    try:
        file_info = os.stat(file_path)
        owner_sid = file_info.st_uid
        print(owner_sid)
        owner_name = None
        with os.popen(f'wmic useraccount where sid="{owner_sid}" get name /value') as stream:
            for line in stream:
                if line.strip():
                    owner_name = line.split('=')[1].strip()
                    break
        return owner_name
    except Exception as e:
        print("Error:", e)
        return None

file_path =(r"C:\\Users\\kisho\\OneDrive\\Desktop\\Python\\contents.rtf")  
owner = get_file_owner(file_path)
if owner:
    print(f"The owner of {file_path} is {owner}.")
else:
    print(f"Failed to retrieve the owner of {file_path}.")
'''
#Name of a file
import os
file_path = ("C:\\Users\\kisho\\OneDrive\\Desktop\\Python\\contents.rtf")
file_name = os.path.basename(file_path)
print("File Name:", file_name)

#File type of a file
def get_file_type(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()
file_type = get_file_type(file_path)
print("File Type:", file_type)

#size,modification time and creation time
file_path=os.stat("C:\\Users\\kisho\\OneDrive\\Desktop\\Python\\contents.rtf")
print(f"size:{file_path.st_size}bytes")
print(f"Modification time:{file_path.st_mtime}")
print(f"creation time:{file_path.st_ctime}")



