from gtts import gTTS

def saveAudio(txt,arq):
	language = 'pt'
	objeto = gTTS(text=txt, lang=language, slow=False)
	objeto.save('/var/www/html/audios/' + arq)
