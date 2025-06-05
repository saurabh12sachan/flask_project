from flask import Flask, render_template


app2=Flask(__name__,template_folder='templates')


# @app2.route('/')
# def index():
#     myvalue='NeuralNine'
#     myresult=10+20
#     return render_template('index.html',myvalue=myvalue,myresult=myresult)

@app2.route('/')
def index():
    mylist={10,20,30,40,50}
    return render_template('index2.html',mylist=mylist)
@app2.route('/other')
def other():
    mylist={10,20,30,40,50}
    return render_template('other.html',mylist=mylist)




if __name__ =='__main__':
    app2.run(host='0.0.0.0' ,debug=True)