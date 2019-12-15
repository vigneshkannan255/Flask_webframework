from flask import Flask,render_template,request

webapp=Flask(__name__) #object creation

@webapp.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		email = request.form['email']
		password = request.form['pass']
		if email == 'abc@gmail.com' and password == 'pass':
			print(email,password)
			return 'login success'


webapp.run(port='8000', debug = True) #calling the run function with object webapp and passing parameter port number and debug 

