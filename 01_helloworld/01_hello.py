from flask import Flask,render_template,request

webapp=Flask(__name__) #object creation

@webapp.route("/") #decorator function
def index():
	return'hello world'


webapp.run(port='8000', debug = True) #calling the run function with object webapp and passing parameter port number and debug 

