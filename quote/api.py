from flask import Flask,render_template,request
from quote_app import quote_day
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        info = quote_day()
        return render_template('home.html',info=info)
    return render_template('home.html')   

if __name__ == "__main__":
    app.run(debug=True)