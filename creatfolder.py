import os
try:
    os.mkdir("python os")
    print("folder created verify")
except FileExistsError:
    print("folder is alredy created")    