# url_buildings.py
'''
✅ What this does:

1️⃣ url_for('about') → Dynamically generates URL for the about route.

2️⃣ url_for('contact', name="Arunesh") → Generates URL for contact route with dynamic parameter.

3️⃣ redirect(url_for(...)) → Redirects to another route dynamically.

4️⃣ Links in HTML are built dynamically so if you change the route later, links still work.

'''



from flask import Flask, url_for, redirect

app = Flask(__name__)
# Home page
@app.route("/")
def home():
    return """
    <h1>Welcome to Home Page</h1>
    <a href="{}">Go to About</a><br>
    <a href="{}">Go to Contact</a>
    """.format(url_for('about'), url_for('contact'))

# About page
@app.route("/about")
def about():
    return """
    <h1>About Page</h1>
    <a href="{}">Go Home</a>
    """.format(url_for('home'))

# Contact page with dynamic parameter
@app.route("/contact/<name>")
def contact(name):
    return f"""
    <h1>Contact Page for {name}</h1>
    <a href="{url_for('home')}">Go Home</a>
    """

# Redirect example
@app.route("/go-to-contact")
def go_to_contact():
    # Redirect to contact page for "Arunesh"
    return redirect(url_for('contact', name="Arunesh"))

if __name__ == "__main__":
    app.run(debug=True)