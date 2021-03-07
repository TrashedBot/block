# http://trashedbot.github.io 2018 The project Trashed
#<p><a href="http://trashed.pw">[Click WEB!]</a></p>

from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from block import *

app = Flask (__name__)

@app.route('/', methods = ['POST','GET'])
def index():

    if request.method == 'POST':
        trashedbot_1 = request.form['trashedbot_1']
        price = request.form['price']
        trashedbot_2 = request.form['trashedbot_2']

        write_block(name=trashedbot_1, amount=price, to_whom=trashedbot_2)
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/checking', methods = ['GET'])
def check():
    results = check_integrity()
    return render_template('index.html', res_dao = results)

if __name__=='__main__':
    app.run(debug=True)
