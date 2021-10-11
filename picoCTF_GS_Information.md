<img align="right" src="https://github.com/0m3g4b1u3/pico-ctf/blob/30c417590719596865c6d2bda53fe3bbef4f12c6/sscLogo200.png" width=64>

# PicoCTF Challenge: Information

Files can always be changed in a secret way. Can you find the flag? cat.jpg

### Hints:

1.  Look at the details of the file
2.  Make sure to submit the flag as picoCTF{XXXXX}

## Solution(s):

_Grab the pic_<br>
`wget https://mercury.picoctf.net/static/c28a959c5605d5f67480d5dd3a77f302/cat.jpg`<br>

Their are many ways to "Look at the details" of a file. We are going to try and do this challenge entirely in the picoCTF webshell so we need to know what commands are available to us. The `compgen -c` command will show you the list we are looking for. This list should prove helpful for future challenges and tasks on linux machines you are unfamiliar with.<br>

After scoping the list we see they have `exiftool`
_Look at the details_<br>
`exiftool cat.jpg`<br>

Lots to look at here, but this challenge focuses on the License. Base64 encryption is rather noticeable because it uses all the upper and lower letters along with the numbers and a few symbols.  
_Decrypt Base64 for flag_
`echo your_license_here | base64 -d`
