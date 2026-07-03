import subprocess
import re
import pyzipper
import base64

# neccessary linux tools
# sudo apt install build-essential ruby-dev
# sudo gem install zsteg
# sudo apt install exiftool

image_path = './images.png'
zip_path = './abc.zip'
alp = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def decypt_caesar(text, reversed=False):
    if reversed:
        text = text[::-1]
    for key in range(1, 25):
        flag_decrypted=''
        for i in text:
            if i.isalpha():
                if i.islower():
                    index = alp.index(i) - key
                    index = index % 26
                    flag_decrypted += alp[index]
                elif i.isupper():
                    index = alp.index(i.lower()) - key
                    index = index % 26
                    flag_decrypted += alp[index].upper()
            else:
                flag_decrypted += i
        match = re.search('CTF{.*}', flag_decrypted)
        if match:
            return match.group(0)

comment = subprocess.run(['exiftool','-Comment', image_path], capture_output=True,text=True,check=True)
print(comment.stdout)

zsteg_out = subprocess.run(['zsteg', image_path], capture_output=True,text=True,check=True)
password = re.search(r'"[a-zA-Z0-9=+/]+=*"', zsteg_out.stdout)

print(zsteg_out.stdout)

passwd = password.group(0)
passwd = passwd.strip('"')
passwd = base64.b64decode(passwd).decode()
print(passwd)

with pyzipper.AESZipFile(zip_path, 'r' ) as zf:
    zf.setpassword(passwd.encode())
    zf.extractall()

file = subprocess.run(['find', '.', '-name', '*.txt' ,'-type', 'f', '-mmin', '-1'], capture_output=True, text=True, check=True).stdout.strip()

with open(file, 'r') as f:
    contents = f.read()
    flag = decypt_caesar(contents, True)

print(f"#### Captured Flag is {flag} ####")





