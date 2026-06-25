from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html", name="John Doe")
@app.route('/about')
def about():
    return 'This is the about page of our Flask app.'
@app.route('/contact')
def contact():
    return 'Contact us at: example@email.com'

if __name__ == '__main__':
    app.run(debug=True)