from flask import Flask,redirect,url_for,request
from Blue_print_route import app_bp
"""
Topic : Routing

desc: Flask routing is the process of mapping a specific URL path to a corresponding Python function (called a view function) that handles the request and returns a response to the client.
it use app.route() decorator to achieve.

Types:
✅ 1️⃣ Static Route
✅ 2️⃣ Dynamic Route (Variable Rule)
        | Converter | Accepts       | Example           | Route Format            |
|-----------|--------------|------------------|-------------------------|
| string    | Text         | /user/Arunesh    | <string:name>           |
| int       | Integer      | /post/10         | <int:id>                |
| float     | Decimal      | /price/99.99     | <float:value>           |
| path      | Text with `/`| /files/a/b.jpg   | <path:filepath>         |
| uuid      | UUID format  | /order/uuid-value| <uuid:unique_id>        |
✅ 3️⃣ Multiple Routes → Same Function
✅ 4️⃣ Redirect Route
✅ 5️⃣ Blueprint Route (Modular Routing)
✅ 6️⃣ Query parameter
"""
app=Flask(__name__)

#1️⃣ Static - fixed url path
@app.route("/home") #home is the url path
def home():
    return "<h1> welcome to home page"

#2️⃣ Dynamic route (variable rule)
#1) string
@app.route("/<name>")
def name(name):
    return f'name :{name}'
#2)int
@app.route("/age/<int:age>")
def age(age):
    return f'age : {age}'

#3) float
@app.route("/float/<float:num>")
def float(num):
    return f'float : {num}'

#4) file path
@app.route('/upload/<path:filepath>')
def file_path(filepath):
    return f'file path : {filepath}'

#4) UUID-value
@app.route('/Id/<uuid:id>')
def UUID(id):
    return f'file path : {id}'


#3️⃣ Multiple route same function


@app.route("/")
@app.route("/Home")
def front_page():
    return "welcome home page"


#4️⃣ redirect route
'''
In flask(), redirect is used to redirect one route to another route

1) redirect() - redirect the page
2)url_for() - create url
'''

# 1️⃣ basic redirect
@app.route("/login/<string:name>/<int:Pass>")
def login(name,Pass):
    if name == "arunesh" and Pass == 5488:
        return redirect("/status")


@app.route("/status")
def status():
    return "login success"

# 2️⃣ redirect url with parameter
'''
create login in authetication and redirect url_for login sucess 
'''

@app.route('/signin/<string:name>/<int:Pass>')
def signin(name,Pass):
    return redirect(url_for("account",name=name,Pass=Pass)) #account is route function name


@app.route('/account_creation/<string:name>/<int:Pass>')
def account(name,Pass):
    return f'name : {name} \n Password {Pass} '


#5️⃣ Blue print route

app.register_blueprint(app_bp,url_prefix="/blue_print")

#6️⃣ Query parameter

'''
In flask query parameter from a URL using the request.args used dictionary like structure.

when used:
1) filter data 
2) passing multiple values
3)sorting
'''

#passing multiple values
@app.route('/details')
def user_details():
    name=request.args.get("name")
    age=request.args.get("age")
    id=request.args.get("id")

    return f'name : {name} age : {age} id : {id}'

if __name__ == "__main__":
    app.run(debug=True)