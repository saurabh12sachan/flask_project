#session and cookies


from flask import Flask,render_template


app3=Flask(__name__,template_folder='templates')

app3.secret_key='Some Key'


@app3.route('/')
def index():
    return render_template('index3.html',message='Index')

@app3.route('/set_data')
def set_data():
    session['name']='mike'
    session['other']='helo world'
    return render_template('index3.html',message='session data set')

if __name__=='__main__':
    app3.run(host='0.0.0.0',debug=True)