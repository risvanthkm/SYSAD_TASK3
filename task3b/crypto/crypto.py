import requests
import hashlib

limit = 9999
salt = "salt"

# storing flag
resp = requests.post(
    "http://localhost:5000/hash",
    json={
        "flag" : "DELTA FORCE INDUCTIONS ;}"
    }
)

hash = resp.json()['hash_value']

for i in range(limit+1):
    pin = str(i).zfill(4)
    pin_with_salt = pin + salt
    hashtry = hashlib.md5(pin_with_salt.encode()).hexdigest()
    if hash == hashtry:
        break
print("-"*5, "Cracked the PIN", pin, "-"*5)
flag = requests.get(
    "http://localhost:5000/get_flag",
    json={
        "pin" : pin
    }
)

print("="*5 ,"The Flag String is:", flag.json()['flag_string'], "="*5, sep='')
