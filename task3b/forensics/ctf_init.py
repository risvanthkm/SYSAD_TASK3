from PIL import Image
from PIL.PngImagePlugin import PngInfo
import base64
import pyzipper

path       = "./images.png"
zip_name   = "abc.zip"
text_name  = "secrets.txt"
passwd     = "passwordforzip"
flag       = "CTF{delta-inductionstask3b-Forensics:)}"
ceasar_key = 3
alp = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def create_zip():
    flag_rev = flag[::-1]
    flag_encrypted = ""
    for i in flag_rev:
        if i.isalpha():
            if i.islower():
                index = alp.index(i) + ceasar_key
                index = index % 26
                flag_encrypted += alp[index]
            elif i.isupper():
                index = alp.index(i.lower()) + ceasar_key
                index = index % 26
                flag_encrypted += alp[index].upper()
        else:
            flag_encrypted += i
    
    with pyzipper.AESZipFile(zip_name, "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(passwd.encode())
        zipf.writestr(text_name, flag_encrypted)

def LSB_modification(image, passwd):
    bits=""
    b64pass = base64.b64encode(passwd.encode()).decode()
    for i in b64pass:
        bits += format(ord(i), "08b")
    width, height = image.size
    pixels = image.load()
    c=0
    no_of_bits = len(bits)
    if height*width*3 < no_of_bits:
        return "Insufficient Image length"
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(bits[c]) if c<no_of_bits else r
            c+=1
            g = (g & ~1) | int(bits[c]) if c<no_of_bits else g
            c+=1
            b = (b & ~1) | int(bits[c]) if c<no_of_bits else b
            pixels[x,y] = (r, g, b)
            c+=1
            if c>=no_of_bits : return

meta = PngInfo()
image = Image.open(path).convert("RGB")

meta.add_itxt("Comment", "Check the least significant bits ;)")

LSB_modification(image, passwd)
create_zip()

image.save(path, pnginfo=meta)

print("### Flag hidden successfully ###")