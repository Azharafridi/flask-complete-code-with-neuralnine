from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    my_list = [10,30,70,30,80]
    return render_template(template_name_or_list = 'index.html',  my_list = my_list)

@app.route('/other')
def other():
    return render_template('other.html')

@app.route('/filters')
def filters():
    some_text = "Hello World"
    return render_template('filters.html', some_text = some_text)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1] 

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5555, debug=True)