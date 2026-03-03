from flask import Flask

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
✅ 4️⃣ Route with HTTP Methods
✅ 5️⃣ Redirect Route
✅ 6️⃣ Blueprint Route (Modular Routing)
"""
app=Flask(__name__)

#Static - fixed url path
@app.route("/home") #home is the url path
def home():
    return "<h1> welcome to home page"




if __name__ == "__main__":
    app.run(debug=True)