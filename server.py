from flask import Flask,render_template,request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
     return render_template(page_name)

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/services.html')
# def services():
#     return render_template('services.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')


# @app.route('/project.html')
# def project():
#     return render_template('project.html')


def write_to_database_txt(data):
	with open('database.txt', mode = 'a') as myfile:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = myfile.write(f'\n{email},{subject},{message}')


def write_to_database_csv(data):
	with open('database.csv', newline='', mode = 'a') as csv_file:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


@app.route('/send_form', methods=['POST', 'GET'])
def send_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		print(data)
		write_to_database_txt(data)
		write_to_database_csv(data)
		return redirect('thank_you.html')
	else:
		return 'something went wrong'
