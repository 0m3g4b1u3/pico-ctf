<img align="right" src="https://github.com/0m3g4b1u3/pico-ctf/blob/30c417590719596865c6d2bda53fe3bbef4f12c6/sscLogo200.png" width=64>

# PicoCTF Challenge: Python Wrangling
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

### Hints:
1.  Get the Python script accessible in your shell by entering the following command in the Terminal prompt:<br>`$ wget https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py`
2. `$ man python`

## Solution(s):
_Get the password._<br>
`$ cat pw.txt`<br><br>
The trick for this is knowing the program requires two arguments. The first argument is either "-d" to decrypt or "-e" to encrypt. The second is the filepath of the file to read.<br>
_Run the program, input password when prompted._<br>
`$ python ende.py "-d" flag.txt.en`<br>
