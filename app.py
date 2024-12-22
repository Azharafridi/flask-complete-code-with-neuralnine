from flask import Flask, request, make_response

app = Flask(__name__)

# end point or routes

@app.route('/') # here defualt is '/'
def index():
    return "<h1>hello world</h1>" # return "hello world"

## add another simple endpoint
@app.route('/hello', methods=['GET','POST', 'PUT'])
def hello():
    if request.method == 'GET':
        return 'You made a GET  request\n'
    elif request.method == 'POST':
        return 'You made a POST request\n'
    return "you will never see this message\n"

## add another route for custom responses
@app.route('/respon')
def hello_response():
    response  = make_response("Hello web user!\n")
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response
## adding dynamic routes mean using a variable name
@app.route('/greet/<name>') # here
def greet(name):
    return f"hello {name}"

@app.route('/add/<int:number1>/<int:number2>') #
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params') # here
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
    else:
        print("some parameters are missing")



if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port = 5555, debug = True) 