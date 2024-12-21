from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    my_list = [10,30,70,30,80]
    return render_template(template_name_or_list = 'index.html',  my_list = my_list)

@app.route('/other')
def other():
    return render_template('other.html')


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5555, debug=True)