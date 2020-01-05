from flask import Flask, request, render_template
from goodreads import client
import os

gc = client.GoodreadsClient(os.environ.get('GCLIENT_TOKEN'),os.environ.get('GCLIENT_KEY'))

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('form.html' )

@app.route('/', methods=['POST'])
def my_form_post():
	try:
		text = request.form['text']
		processed_text = int(text.strip())
		links = gc.book(processed_text).similar_books[:7]
		links.insert(0,gc.book(processed_text))
		print(links)
		return render_template('index.html', len = 7, links=links)
	except:
		return render_template('404.html')
	
if __name__=="__main__":
	app.run()


