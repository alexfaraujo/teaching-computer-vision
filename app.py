from text_reader import read_text
from flask import Flask, request
from flask_cors import CORS, cross_origin

# instantiate Flask object
meu_app = Flask(__name__)

# activate CORS to initialized Flask object
cors = CORS(meu_app)
meu_app.config['CORS_HEADERS'] = 'Content-Type'

# define folder to store uploaded files
meu_app.config['UPLOAD_FOLDER'] = 'static/files'

token = '123456'

@meu_app.route('/enviar_imagem', methods=['POST'])
@cross_origin()
def enviar_imagem():
    if request.method == 'POST':
        if request.form['token'] == token:
            f = request.files['file']
            url_file = f'{meu_app.config["UPLOAD_FOLDER"]}/{f.filename}'
            f.save(url_file)
            response = read_text(url_file)

            return response
        return '{"msg": "token incorrect"}'
    return '{"msg": "method not allowed"}'


if __name__ == '__main__':
    meu_app.run(debug=True, host='0.0.0.0')
