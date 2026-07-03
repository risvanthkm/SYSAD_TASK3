from flask import Flask, request, make_response, jsonify
import hashlib

app = Flask(__name__)
salt = "salt"
pin  = 2003 # year when delta force started ;)

@app.route("/hash", methods=['POST'])
def flag():
    global flag
    data = request.json
    flag = data["flag"]
    dgst = hashlib.md5((str(pin)+salt).encode()).hexdigest()
    return {
        "hash_value" : dgst
    }

@app.route("/get_flag", methods=['GET'])
def get_flag():
    data = request.json
    u_pin = data["pin"]
    if int(u_pin) == int(pin):
        return {"flag_string": flag}
    return {"error" : "invalid pin"}, 401

if __name__ == "__main__":
    app.run(debug=True)


