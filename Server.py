from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('frontend.html')
'''@app.route('/works.html')
def works():
    return render_template('works.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/contact.html')
def contacts():
    return render_template('contact.html')
@app.route('/work.html')
def work():
    return render_template('work.html')
@app.route('/work2.html')
def work2():
    return render_template('work2.html')
@app.route('/work3.html')
def work3():
    return render_template('work3.html')
@app.route('/work4.html')
def work4():
    return render_template('work4.html')
@app.route('/<name>')
def page_identity(name=None):
    return render_template(name)
'''
def write_to_file(data):
    with open('database.txt','a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n Email: {email}\n Subject: {subject}\n Message: {message} \n ')

def write_to_csv(data):
    with open('database.csv','a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
'''
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('error.html')
        except:
            return'something went wrong try again'
    else:
        return redirect('submit.html')
'''
