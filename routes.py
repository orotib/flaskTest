from flask import Flask, render_template, request
from models import db
from forms import SignupForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost/test'
db.init_app(app)

app.secret_key = 'development-key'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:
			return 'Success!'
	elif request.method == 'GET':
		return render_template('signup.html', form=form)

########################

if __name__ == '__main__':
	app.run(debug=True, host='192.168.1.130')
