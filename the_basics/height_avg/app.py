from flask import Flask ,render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func  
from werkzeug.utils import secure_filename
import os
from my_files import show_file

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:post123@localhost/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id= db.Column(db.Integer,primary_key= True)
    email_ = db.Column(db.String(120),unique=True)
    height_ = db.Column(db.Integer)
    
    def __init__(self,email_,height_):
        self.email_ = email_
        self.height_ = height_
        
        




@app.route('/')
def index():
    return render_template("index.html")


@app.route('/success', methods=['POST','GET'])
def success():
    if request.method == 'POST':
        try:
            email = request.form['email_name']
            height = request.form['height_name']
            data = Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg = db.session.query(func.avg(Data.height_)).scalar()
            count = db.session.query(Data.height_).count()
            send_email(email,height,avg,count)
            return render_template("success.html")
        except Exception as e:
            print("\n\n\n>>>>>>>>>Error Error Error Error: \n", e.args)
            if "already exists" in str(e.args[0]):
                print("EMAIL ALREADY EXISTS Ahmed")
                return render_template("index.html",error_email= "Email already exists")
                #return render_template("error.html",value= "EMAIL ALREADY EXISTS")
            else:
                return render_template("error.html",value= "Something Wrong")
    else:
        return render_template("error.html",value= "Something Wrong")
        
        
@app.route('/upload' ,methods=['POST'])
def upload():
    global uploaded_file
    if request.method == "POST":
        uploaded_file = request.files["file_name"]
        uploaded_file_name = secure_filename("uploaded-" + uploaded_file.filename)
        uploaded_file.save(uploaded_file_name)
        return render_template("index.html" , btn='download.html',file_name = uploaded_file_name )


@app.route('/error' ,methods=['POST'])
def error():
    return render_template("error.html")

@app.route('/download')
def download():
    return show_file(uploaded_file= uploaded_file , as_attachment= True)
    


@app.route('/show')
def show():
    return show_file(uploaded_file= uploaded_file , as_attachment= False)
    


if __name__ == '__main__':
    app.debug =True
    app.run()