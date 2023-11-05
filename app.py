from text_reader import read_text
from flask import Flask, request

meu_app = Flask(__name__)

meu_app.config['UPLOAD_FOLDER'] = 'static/files'


@meu_app.route('/enviar_imagem', methods=['POST'])
def enviar_imagem():
    if request.method == 'POST':
        f = request.files['file']
        url_file = f'{meu_app.config["UPLOAD_FOLDER"]}/{f.filename}'
        f.save(url_file)
        response = read_text(url_file)

        return response
    return None


if __name__ == '__main__':
    meu_app.run(debug=True, host='0.0.0.0')
