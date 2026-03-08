from flask import Flask,Blueprint

app_bp=Blueprint('blue_print',__name__) #blue_print is a blueprint name

@app_bp.route('/')
def bp():
    return "welcome to blue print page"

