from flask import Flask,render_template

"""
Notes:
1) Flask automatically connect look  folder name "template"

keyway:
1️⃣ Basic
2️⃣ Passing Data to Html
3️⃣ Multiple Variables
4️⃣ Rendering Inside Loop
5️⃣ Passing Data in dictionary variables
6️⃣ Control Structure

Important Rules
    - HTML files must be inside templates folder
    - render_template() automatically looks in that folder
    - Uses Jinja syntax ({{ }} and {% %})
"""
app=Flask(__name__,template_folder="templates") #connect manually

#1️⃣ Basic
@app.route('/login')
def login():
    return render_template("login.html")

#2️⃣ Passing Data to Html
@app.route("/user")
def user():
    name="arunesh"
    return render_template("user.html",username=name)

#5️⃣ Passing Data in dictionary variables
@app.route("/user_details")
def details():
    user={
        "name":"Arunesh",
        "Age": 23,
        "id":406,
    }
    return render_template("user.html",User=user)


if __name__ == "__main__":
    app.run(debug=True)