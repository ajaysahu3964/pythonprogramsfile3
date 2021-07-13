import re 
matinfo =re.finditer("kvr","aG7672369CUKP)v$3KhjyVMCErk")
print("_----------------------------_")
for mat in matinfo:
    print("start index:{}\tvalue:{}".format(mat.start(),mat.group()))
else:
    print("__---------------------------__")