from flask import Flask, render_template,request
import os

UPLOAD_FOLDER = '/desktop/real_rash_project/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
 	if request.method == 'POST':
		file = request.files['file']
		filename = file.filename
		filename = 'output' + '.jpg'
		print(file,filename)
		file.save('./uploads/'+filename)
		return filename
	return render_template('index.html')

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

