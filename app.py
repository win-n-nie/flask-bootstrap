from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def spoiler():
    return render_template('spoilers.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bootstrap')
def bootstrap():
    return render_template('signin.html')
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
