from flask import Flask,request
app=Flask(__name__)



@app.route('/')

def index():
    return "<h1>Hello World</h1>"


@app.route('/hello')

def hello():
    return "<h1>Hello World</h1>"







@app.route('/greet/<name>')
def hello1(name):
    return f"hello1 {name}"

@app.route('/add/<numb1>/<numb2>')
def add(numb1,numb2):
    return f"{numb1}+{numb2}={numb1+numb2}"


#if we want to add then we have to typecst inside the variable

@app.route('/add1/<int:numb1>/<int:numb2>')
def add1(numb1,numb2):
    #here f used to embed the string in view   to embed use{}
    return f"{numb1}+{numb2}={numb1+numb2}"


@app.route('/handle_url_params1')
def handle_params1():
    return str(request.args) #it give output in dictionary
#request.args is a MultiDict (multi-value dictionary) that holds the query parameters of the request (i.e. values in the URL after the ?).


@app.route('/handle_url_params2')
def handle_params2():
    greeting=request.args['greeting']
    name=request.args.get('name')
    return f'{greeting},{name}'
#input=http://127.0.0.1:5555/handle_url_params2?greeting=hello&name=saurabh
#output=hello,saurabh

#if any of the args missing then---

@app.route('/handle_url_params23')
def handle_params23():
    if 'greet' in request.args.keys() and 'name1' in request.args.keys():
        greet=request.args['greet']
        name1=request.args.get('name1')
        return f'{greet},{name1}'
    else:
        return 'Some parameters are missing'
#input=http://127.0.0.1:8000/handle_url_params23?name1=mike&greet=hello
#output=hello,mike
#input=http://127.0.0.1:8000/handle_url_params23?name1=mike
#output=Some parameters are missing

#above all route only handle by default get request.



#how to handle post request in powershell -------

#in powershell
# #(base) PS C:\Users\ssach> curl.exe http://127.0.0.1:8000/hello
# <!doctype html>
# <html lang=en>
# <title>404 Not Found</title>
# <h1>Not Found</h1>




# so use post inside the @app.route--
@app.route('/hello3', methods=['POST','GET'])

def hello3():
    return "<h1>Hello World</h1>"
#input in powershell=
# input=curl.exe -X POST http://127.0.0.1:8000/hello
# output=<h1>Hello World</h1>

@app.route('/hello4', methods=['POST','GET'])

def hello4():
    if request.method=="GET":
        return "u made a get request"
    elif request.method=="POST":
        return "u made  a POST request"
    else: 
        return "u will never see this message"
#input in powershell=


if __name__ == '__main__':
    app.run(host='0.0.0.0',port =8000, debug =True ) 