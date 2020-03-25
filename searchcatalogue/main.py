from flask import Flask,request
from flask_cors import CORS
import mongo as m
from searchcatalogue import catalogue as c
from searchcatalogue import searchlog as sl
import time
from bson.json_util import dumps



app = Flask(__name__)
CORS(app)

note_dict=dict()
pr_name = ""

@app.route('/mongodbcall',methods=['GET','POST'])
def mongodbcall():

    pr_name = request.form.get('str1user')
    print(pr_name)
    t1=time.time()
    sl.searchlogg(pr_name,t1)
    x=m.mongo_ext(pr_name)
    #c.cataloguee(x)


    return x





if __name__ == '__main__':
    app.run(host='3.82.157.77', port=5000, debug=False)
