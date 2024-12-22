import uuid
import os
import pandas as pd
from flask import Flask, request, Response, render_template, send_from_directory, jsonify

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
    
# contverting text file into csv files
@app.route('/convert_to_csv', methods=['POST'])
def convert_to_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(), 
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename = result.csv'
        }
        )
    return response


@app.route('/convert_csv_two', methods = ['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template(template_name_or_list='download.html', filename=filename)
 
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(directory = 'downloads', path=filename) # , download_file = 'result.csv'


## endpoints for javascript, we expect to be a json data here
@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']
    
    with open('file.txt', 'w') as f:
        f.write(f'{greeting} {name}')

    return jsonify({'message': 'Successfully written!'})



if __name__ == '__main__':
    app.run(host='0.0.0.0',  debug=True)
    