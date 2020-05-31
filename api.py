from flask import Flask
from flask import request
from flask import send_from_directory
from audio import saveAudio

app = Flask(__name__)

@app.route("/")
def init():
	return "<h1>API em Python com Flask</h1><br><b>/audio</b><br>Argumentos:<br>texto = texto a ser convertido<br>nome_arquivo = nome arquivo de audio a ser recuperado<br><br><b>Exemplo:</b><br>/audio?texto=oi&nome_arquivo=audio"

@app.route('/audio', methods=['GET'])
def audio():
	p = request.args
	txt = p.get('texto')
	arquivo = p.get('nome_arquivo') + '.mp3'
	saveAudio(txt,arquivo)
	return send_from_directory('/var/www/html/',filename=arquivo,as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1>Recurso nao encontrado."

if __name__ == "__main__":
	app.run()
