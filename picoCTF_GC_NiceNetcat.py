"""#############################################################################
##  PROGRAM:    Nice Netcat...
##  FILENAME:   picoCTF_GC_NiceNetcat.py
##  AUTHOR:     Om3g4b1u3
#############################################################################"""
##  VARIABLE(S)  ##
file_path = "flag_NiceNetcat.text"
flag = ""

##  PROGRAM START  ##
encr_flag = open(file_path).readlines()
for ltr in encr_flag: flag += chr(int(ltr.strip()))
print(flag)
