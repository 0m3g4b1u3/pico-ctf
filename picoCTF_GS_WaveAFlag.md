<img align="right" src="https://github.com/0m3g4b1u3/pico-ctf/blob/30c417590719596865c6d2bda53fe3bbef4f12c6/sscLogo200.png" width=64>

# PicoCTF Challenge: Wave A Flag

Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

### Hints:

1.  This program will only work in the webshell or another Linux computer.
2.  To get the file accessible in your shell, enter the following in the Terminal prompt:<br>`$ wget https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm`
3.  Run this program by entering the following in the Terminal prompt:<br>`$ ./warm, but you'll first have to make it executable with $ chmod +x warm`
4.  `-h` and `--help` are the most common arguments to give to programs to get more information from them!
5.  Not every program implements help features like `-h` and `--help`.

## Solution(s):

### Using their hints...

_Literally just follow the hints._

### The Easy Way

`$ strings warm | grep picoCTF`
