"""#####################################################################
##	PROGRAM:	Mod 26
##	FILENAME:	picoCTF_Mod26.py
##	AUTHOR:		Om3g4b1u3
#####################################################################"""
import string

encrypted_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"

def rotN(msg, n, mode):
	new_msg= ""
	if(mode=="e"):
		for ltr in msg:
			if(ltr in string.ascii_letters):
				tmp = string.ascii_letters.find(ltr)
				new_msg += string.ascii_letters[(tmp+n)%26]
			else:
				new_msg += ltr
	else:
		new_msg = rotN(msg, 26-n, "e")
	return new_msg

print(rotN(encrypted_flag, 13, "d"))

#picoctf{next_time_i'll_try_2_rounds_of_rot13_afxtzqwr}
