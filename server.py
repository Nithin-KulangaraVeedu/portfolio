from flask import Flask, render_template,request,redirect
app = Flask(__name__) #instance of flask app

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as db:
        email = data['email']
        subject= data['subject']
        message = data['message']
        db.write(f'{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' :
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

