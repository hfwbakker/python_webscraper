from flask import Flask, render_template,url_for
import asf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/axios')
def axios():
    return render_template("axios.html")

@app.route('/axios_scraper')
def axios_scraper():
    return render_template("axios_scraper.py")

@app.route('/asf')
def asf():
    return asf.user_selection()

if __name__ == "__main__":
    app.run(debug=True)