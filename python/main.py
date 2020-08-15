from flask import Flask, request, render_template
import analyse as an

app = Flask(__name__)

# @app.before_request
# def load_analyser():
processor = an.Analyse()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    #processed_text = text.upper()

    processed_text = processor.processText(text) # call to Analyse object
    return processed_text

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='80')
