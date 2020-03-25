from flask import Flask,request
from flask_cors import CORS
import mongo as m

import time
from bson.json_util import dumps



app = Flask(__name__)
CORS(app)

note_dict=dict()
pr_name = ""


@app.route('/usernote',methods=['POST'])
def usernote():
    print(pr_name)
    notedata = request.form.get('notes')
    keyname= request.form.get('search')
    print(keyname)
    print(pr_name)

    if keyname in note_dict:
        note_dict[keyname] += ' '+ notedata
    else:
        note_dict[keyname] = ' ' + notedata

    f=open("usernote.json","w+")
    f.write(dumps(note_dict))

    print(dumps(note_dict))
    return dumps(note_dict)

@app.route('/retrievenote',methods=['GET','POST'])
def retrievenote():
    ls=[]
    notess = request.form.get('search')

    print(notess)

    print(note_dict)
    for key,values in note_dict.items():
        if notess == key:
            ls.append(values)
    print(ls)
    return dumps(ls)



if __name__ == '__main__':
    app.run(host='3.82.157.77', port=5001, debug=False)
