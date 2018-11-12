from flask import Flask, request, jsonify
import zeroConf as ZC
import AuthDB as DB
import json
from werkzeug.utils import secure_filename
import os

cwd = os.getcwd()
UPLOAD_FOLDER = cwd+'/uploadedFiles/'
ALLOWED_EXTENSIONS = set(['txt', '.sh', '.py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = DB.DBClass()


PORT = 5000

@app.route("/add_user", methods=['POST'])
def exeADD_USER():
    form = (request.get_json())
    d = {}
    d['username'] = form.get('username')
    d['password'] = form.get('password')
    res = db.addUser(d);
    return jsonify(response=res)


@app.route("/upload/<action>", methods=['POST', 'GET'])
def exeUPLOAD(action=None):
    auth = request.authorization
    valid_user = db.findPerson(auth)
    if not valid_user:
        return jsonify(error='Invalid credentials')
    if 'file' not in request.files:
        flash('No file part')
        return jsonify(error="No file given")
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return jsonify(error="No file given")
    if file:
        filename = secure_filename(file.filename)
        file.save((UPLOAD_FOLDER+filename))
        
        print("Executing file...")
        if action == "led":
            command = "bash {}{} {}".format(UPLOAD_FOLDER,filename, str(ZC.LED_IP))
            os.system(command)
            return jsonify(Message="LED file uploaded")
        else:
            command = "bash {}{} {}".format(UPLOAD_FOLDER,filename, str(ZC.STORAGE_IP))
            os.system(command)
            return jsonify(Message="Storage file uploaded")


@app.route("/")
def homeDir():
    return ("[Home Dir : '/']")





if __name__ == "__main__":
    ZC.startZeroconf()
    print("Server is running...")    
    app.run(host='0.0.0.0', port=5000, debug=False)
    db.delete()
    print('Database cleared')

