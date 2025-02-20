from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("profile"))

@app.route("/profile")
def profile():
    return render_template("index.html", name="Tran Van Hoang")

@app.route("/static/<path:file_path>")
def files(file_path):
    return url_for('static', filename=file_path)

if __name__=="__main__":
    app.run(debug=True) 