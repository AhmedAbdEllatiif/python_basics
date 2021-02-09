from flask import Flask,send_file,render_template,request
from my_files import handle_file,save_file


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods= ['POST','GET'])
def streambyte():
    if request.method == 'POST':
        global converted_file
        uploaded_file = request.files["input_file_name"] 
        uploaded_file.save(uploaded_file.filename)
        bol,obj = handle_file(uploaded_file)
        
        # check if bol is true draw the table
        if bol:
            converted_file = obj 
            return render_template('index.html', downlaod= "download.html",table =obj.to_html(),thanks_text= "Thanks for using our app!!!" )
        else: 
            return render_template('index.html',error_text = str(obj))
        

@app.route('/download-file')
def download():
    return save_file()

if __name__ == '__main__':
    app.debug =True
    app.run()