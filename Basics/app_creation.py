from flask import Flask #import libray

app=Flask(__name__)#Flask is the class create the application is a object
"""  without __name__ flask wouldnt find the where is template and static folder"""

@app.route("/")
def home():
	return "<h1>welcome to home page</h1>"

if __name__ == "__main__": #run when app directly called
	app.run(debug=True)