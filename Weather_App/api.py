from flask import Flask,render_template,request
from weather_info import weather
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        info = weather(city)
        return render_template('home.html',info=info)
    return render_template('home.html')   

if __name__ == "__main__":
    app.run(debug=True)