from flask import Flask
import database
import datetime
import time
from flask import render_template

app = Flask(__name__)
def Reverse(lst): 
    return [ele for ele in reversed(lst)] 
def build():
    Connection = database.connect()
    currenttime = datetime.datetime.now()
    temp = database.get_test_by_time(Connection,currenttime)
    # print ("temp size.", temp.count())
    return temp

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    j=0
    while 1:
        return render_template('index.html',items=build())
if __name__ == '__main__':
    print('Server is runing')
    app.run()

