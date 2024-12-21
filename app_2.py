import pandas as pd
from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index_2():
    if request.method == 'GET':
        return render_template('index_2.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            return 'Success login'
        else:
            return 'Fail login'
        

# endpoints for upload_file of files
@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)