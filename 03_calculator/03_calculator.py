from flask import Flask,render_template,request

webapp=Flask(__name__) #object creation

@webapp.route('/cal',methods=['GET','POST'])
def cal():
	if request.method == 'GET':
		return render_template('cal.html')
	else:
		a = request.form['a']
		b = request.form['b']
		operand = request.form['operand']
		if operand == '+':
			c = int(a)+int(b)
			return str(c)
		elif operand == '-':
			c = int(a)-int(b)
			return str(c)
		elif operand == '*':
			c = int(a)*int(b)
			return str(c)
		elif operand == '/':
			c = int(a)/int(b)
			return str(c)

webapp.run(port='8000', debug = True) #calling the run function with object webapp and passing parameter port number and debug 

