from flask import Flask,request, render_template
app=Flask(__name__)
@app.route('/input')
def input_page():
    return render_template("input.html")
@app.route('/submit', methods=['POST'])
def submit():
    name=request.form["name"]
    email=request.form["email"]
    return f"Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)