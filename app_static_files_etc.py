from flask import Flask, render_template


app =  Flask(__name__, template_folder="templates", static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('index_static.html')

# here is the endpoint for bootstrap
@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrip_css_js.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)