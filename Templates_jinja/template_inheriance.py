"""
1) Template inheritance used for reuse the same html code for multiple page avoid repeating code

"""


from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("template_inheritance/home.html")



if __name__ =="__main__":
    app.run(debug=True)