from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import os
import psycopg2

app = Flask(__name__)

# calorie-counter-320901 is personal project id
# postgresql-regular-89461

DATABASE_URL = os.environ.get('DATABASE_URL')

mytotalcalories = 0

def get_db_connection():
	try:
	    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
	    return conn
	except:
	    print("ERROR")
	    sys.exit(1)




@app.route("/")
def index():

	return render_template('index.html')



@app.route("/calcclear", methods=["GET", "POST"])
def calcclear():
	if request.method == "POST":

		try: 
			conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		except:
			return "1"
		try:
			cur = conn.cursor()
		except:
			return "2"

		try:
			cur.execute("UPDATE calorielog set myserving = NULL where myserving is not null")
		except:
			print("Error1")

		try:
			conn.commit()
		except:
			return "4"

		cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving, myserving, mycalories FROM calorielog ORDER BY food")
		calorielog = cur.fetchall()


		# set total calories var


		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except:
			print("Error2")


		conn.close()
		return render_template('calccal.html', calorielog = calorielog, mytotalcalories = mytotalcalories)


		# end

	else:
		try:
			cur.execute("SELECT * FROM calorielog")
		except:
			print("Error3")

		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except:
			print("Error4")


		
		conn.close()
		return render_template('calccal.html', calorielog=calorielog, mytotalcalories = mytotalcalories)


@app.route("/calccal", methods=["GET", "POST"])
def calccal():
	if request.method == "POST":
		try:
			foodname = request.form['foodname']
			myserving = request.form['myserving']
			try: 
				conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"

			try:
			 	cur.execute("UPDATE calorielog set myserving = '{}' WHERE food = '{}'".format(myserving, foodname))
			except:
				print("Error5")

		

			try:
				conn.commit()
			except:
				print("Error6")



			try:
				cur.execute("SELECT * FROM calorielog ORDER BY food")
			except:
				print("Error7")


			calorielog = cur.fetchall()

			try:
				cur.execute("SELECT sum(mycalories) FROM calorielog")
				mytotalcalories = cur.fetchone()[0]
			except:
				print("Error8")
				

			conn.close()

			return render_template('calccal.html', calorielog = calorielog, mytotalcalories = mytotalcalories)


		# end
		except:
			print("Error9")
			return "Database Connection Error"
			return render_template('calccal.html')

	else:
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()

		cur.execute("SELECT * FROM calorielog ORDER BY food")
		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except:
			print("Error10")

		conn.close()
		return render_template('calccal.html', calorielog = calorielog, mytotalcalories = mytotalcalories)

@app.route("/addfood", methods=["GET", "POST"])

def addfood():
	print("addfood", request.method)


	if request.method == "POST":
		try:
			foodname = request.form['foodname']
			serving1 = request.form['serving1']
			serving2 = request.form['serving2']
			calories1 = request.form['calories1']

			try: 
				conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"
			try:
			 	cur.execute("INSERT INTO calorielog VALUES (%s, %s, %s, %s)",
			 	(foodname, serving1, serving2, calories1))
			
			except:
				print("Error11")
			try:
				conn.commit()
			except:
				print("commit add food failed")

			cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving FROM calorielog ORDER BY food")
			calorielog = cur.fetchall()
			conn.close()
			return render_template('food.html', calorielog = calorielog)


		# end
		except:
			print("Error12")
			return "Database Connection Error"
			return render_template('addfood.html')

	else:
		return render_template('addfood.html')



@app.route("/deletefood", methods=["GET", "POST"])
def deletefood():

	if request.method == "POST":
		try:
			foodnamedel = request.form['foodnamedel']

			try: 
				conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"

			try:
			 	cur.execute("DELETE FROM calorielog WHERE food = '{}'".format(foodnamedel))
			except:
				print("Error11")
			try:
				conn.commit()
			except:
				print("commit delete food failed")

			cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving FROM calorielog ORDER BY food")
			calorielog = cur.fetchall()
			conn.close()
			return render_template('food.html', calorielog = calorielog)


		# end
		except:
			print("Error12")
			return "Database Connection Error"
			return render_template('deletefood.html')

	else:
		return render_template('deletefood.html')











@app.route("/food", methods=["GET", "POST"])
def food():
	mytotalcalories = 0
	if request.method == "POST":
		foodname = request.form['foodname']
		serving1 = request.form['serving1']
		serving2 = request.form['serving2']
		calories1 = request.form['calories1']
		myserving = request.form['myserving']

		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()

		try:
			cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
			servingsize, servinggrams, caloriesperserving, foodname))
		except:
			print("Error writing food")
		# selects all again updated

		try:
			cur.execute("SELECT * FROM calorielog ORDER BY food")
		except:
			print("Error14")

		calorielog = cur.fetchall()

		conn.close()

		# end
		return render_template('food.html', calorielog=calorielog)

	else:		
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		
		try:
			cur.execute("SELECT * FROM calorielog ORDER BY food")
		except:
			print("Error15")

		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog ORDER BY food")
			mytotalcalories = cur.fetchone()[0]
		except:
			print("Error16")


		conn.close()



		return render_template('food.html', calorielog=calorielog, mytotalcalories = mytotalcalories)



@app.route("/deletediarylog", methods=["GET", "POST"])

def deletediarylog():

	print("deletediarylog", request.method)


	if request.method == "POST":
		try:
			datex = request.form['date']

			if not datex:
				return "You must input a date."


			try: 
				conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			except:
				return "1"
			
			
			try:
				cur = conn.cursor()
			except:
				return "2"

			



			try:	
				cur.execute("DELETE FROM diary WHERE date = ('{}')".format(datex))
				print("deleted")
			except:
				print("diary error 1")

			

			try:
				conn.commit()
				print("committed")
			except:
				print("commit diary delete failed")


			try:
				cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
			except:
				print("diary get failed")
				
			diary = cur.fetchall()
			conn.close()
			return render_template('diary.html', diary = diary)


		# end
		except:
			return "Database Connection Error"
			return render_template('adddiarylog.html')

	else:
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		
		try:
			cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		except:
			print("errorr")

			
		diary = cur.fetchall()

		conn.close()

		return render_template('deletediarylog.html', diary=diary)




@app.route("/adddiarylog", methods=["GET", "POST"])

def adddiarylog():

	print("adddiarylog", request.method)


	if request.method == "POST":
		datex = request.form['date']

		if not datex:
			return "You must input a date."


		weightx = request.form['weight']
		exercisedx = request.form['exercised']
		overatex = request.form['overate']
		breakfastx = request.form['breakfast']
		lunchx = request.form['lunch']
		dinnerx = request.form['dinner']
		snack1x = request.form['snack1']
		snack2x = request.form['snack2']
		snack3x = request.form['snack3']
		snack4x = request.form['snack4']
		snack5x = request.form['snack5']
		snack6x = request.form['snack6']
		bcalories = int(request.form['bcalories'])
		lcalories = int(request.form['lcalories'])
		dcalories = int(request.form['dcalories'])
		s1calories = int(request.form['s1calories'])
		s2calories = int(request.form['s2calories'])
		s3calories = int(request.form['s3calories'])
		s4calories = int(request.form['s4calories'])
		s5calories = int(request.form['s5calories'])
		s6calories = int(request.form['s6calories'])

		try: 
			conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		except:
			return "1"

		try:
			cur = conn.cursor()
		except:
			return "2"
		
		try:
			cur.execute("SELECT * FROM diary WHERE date = '{}'".format(datex))
			date = cur.fetchone()[0]
			if date is not None:
				return "That date has already been used."
			else:
				print("date not used")
		except:
			print("date used error")



		try:	

			cur.execute("INSERT INTO diary (date) VALUES ('{}')".format(datex))
			print("date written")
		except:
			print("diary error 1")

		try:
			conn.commit()
			print("committed")
		except:
			print("commit diary log failed")


		if weightx:

			try:
				cur.execute("UPDATE diary SET weight = '{}' where date ='{}'".format(weightx, datex))
				print("w")
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 2")

		if exercisedx:
			try:
				cur.execute("UPDATE diary SET exercised = '{}' where date ='{}'".format(exercisedx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")

			except:
				print("diary error 3")

		if overatex:
			try:
				cur.execute("UPDATE diary SET overate = '{}' where date ='{}'".format(overatex, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")

			except:
				print("diary error 4")

		if breakfastx:
			try:
				cur.execute("UPDATE diary SET breakfast = '{}' where date ='{}'".format(breakfastx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 5")

		if lunchx:
			try:
				cur.execute("UPDATE diary SET lunch = '{}' where date ='{}'".format(lunchx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 6")

		if dinnerx:
			try:
				cur.execute("UPDATE diary SET dinner = '{}' where date ='{}'".format(dinnerx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 7")

		if snack1x:		
			try:
				cur.execute("UPDATE diary SET snack1 = '{}' where date ='{}'".format(snack1x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 8")
		if snack2x:
			try:
				cur.execute("UPDATE diary SET snack2 = '{}' where date ='{}'".format(snack2x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 9")

		if snack3x:
			try:
				cur.execute("UPDATE diary SET snack3 = '{}' where date ='{}'".format(snack3x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 10")

		if snack4x:
			try:
				cur.execute("UPDATE diary SET snack4 = '{}' where date ='{}'".format(snack4x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 11")

		if snack5x:
			try:
				cur.execute("UPDATE diary SET snack5 = '{}' where date ='{}'".format(snack5x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 12")

		if snack6x:
			try:
				cur.execute("UPDATE diary SET snack6 = '{}' where date ='{}'".format(snack6x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 13")

		if int(bcalories) > 0:
			try:
				cur.execute("UPDATE diary SET bcalories = {} where date ='{}'".format(bcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 14")

		if int(lcalories) > 0:
			try:
				cur.execute("UPDATE diary SET lcalories = {} where date ='{}'".format(lcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 15")

		if int(dcalories) > 0:
			try:
				cur.execute("UPDATE diary SET dcalories = {} where date ='{}'".format(dcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 16")

		if int(s1calories) > 0:
			try:
				cur.execute("UPDATE diary SET s1calories = {} where date ='{}'".format(s1calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 17")

		if int(s2calories) > 0:
			try:
				cur.execute("UPDATE diary SET s2calories = {} where date ='{}'".format(s2calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 18")

		if int(s3calories) > 0:
			try:
				cur.execute("UPDATE diary SET s3calories = {} where date ='{}'".format(s3calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 19")

		if int(s4calories) > 0:
			try:
				cur.execute("UPDATE diary SET s4calories = {} where date ='{}'".format(s4calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 20")

		if int(s5calories) > 0:
			try:
				cur.execute("UPDATE diary SET s5calories = {} where date ='{}'".format(s5calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 21")

		if int(s6calories) > 0:
			try:
				cur.execute("UPDATE diary SET s6calories = {} where date ='{}'".format(s6calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 22")


		try:
			conn.commit()
			print("committed")
		except:
			print("commit diary log 2 failed")

		try:
			cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		except:
			print("diary get failed")
		diary = cur.fetchall()
		conn.close()
		return render_template('diary.html', diary = diary)


		# end
		

	else:
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		try:
			cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		except:
			print("error")
		diary = cur.fetchall()

		conn.close()

		return render_template('adddiarylog.html', diary=diary)

@app.route("/updatediarylog", methods=["GET", "POST"])

def updatediarylog():

	if request.method == "POST":
		datex = request.form['date']

		if not datex:
			return "You must input a date."


		weightx = request.form['weight']
		exercisedx = request.form['exercised']
		overatex = request.form['overate']
		breakfastx = request.form['breakfast']
		lunchx = request.form['lunch']
		dinnerx = request.form['dinner']
		snack1x = request.form['snack1']
		snack2x = request.form['snack2']
		snack3x = request.form['snack3']
		snack4x = request.form['snack4']
		snack5x = request.form['snack5']
		snack6x = request.form['snack6']
		bcalories = int(request.form['bcalories'])
		lcalories = int(request.form['lcalories'])
		dcalories = int(request.form['dcalories'])
		s1calories = int(request.form['s1calories'])
		s2calories = int(request.form['s2calories'])
		s3calories = int(request.form['s3calories'])
		s4calories = int(request.form['s4calories'])
		s5calories = int(request.form['s5calories'])
		s6calories = int(request.form['s6calories'])

		try: 
			conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		except:
			return "1"

		try:
			cur = conn.cursor()
		except:
			return "2"
		
		try:
			cur.execute("SELECT * FROM diary WHERE date = '{}'".format(datex))
			date = cur.fetchone()[0]
			if date is None:
				return "That date has not yet been recorded. Add in the diary entry first."
			else:
				print("date used")
		except:
			print("date not used")


		if weightx:

			try:
				cur.execute("UPDATE diary SET weight = '{}' where date ='{}'".format(weightx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 2")

		if exercisedx:
			try:
				cur.execute("UPDATE diary SET exercised = '{}' where date ='{}'".format(exercisedx, datex))
				print("e")
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")

			except:
				print("diary error 3")

		if overatex:
			try:
				cur.execute("UPDATE diary SET overate = '{}' where date ='{}'".format(overatex, datex))
				print("o")
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")

			except:
				print("diary error 4")

		if breakfastx:
			try:
				cur.execute("UPDATE diary SET breakfast = '{}' where date ='{}'".format(breakfastx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 5")

		if lunchx:
			try:
				cur.execute("UPDATE diary SET lunch = '{}' where date ='{}'".format(lunchx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 6")

		if dinnerx:
			try:
				cur.execute("UPDATE diary SET dinner = '{}' where date ='{}'".format(dinnerx, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 7")

		if snack1x:		
			try:
				cur.execute("UPDATE diary SET snack1 = '{}' where date ='{}'".format(snack1x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 8")
		if snack2x:
			try:
				cur.execute("UPDATE diary SET snack2 = '{}' where date ='{}'".format(snack2x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 9")

		if snack3x:
			try:
				cur.execute("UPDATE diary SET snack3 = '{}' where date ='{}'".format(snack3x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 10")

		if snack4x:
			try:
				cur.execute("UPDATE diary SET snack4 = '{}' where date ='{}'".format(snack4x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 11")

		if snack5x:
			try:
				cur.execute("UPDATE diary SET snack5 = '{}' where date ='{}'".format(snack5x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 12")

		if snack6x:
			try:
				cur.execute("UPDATE diary SET snack6 = '{}' where date ='{}'".format(snack6x, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 13")

		if int(bcalories) > 0:
			try:
				cur.execute("UPDATE diary SET bcalories = {} where date ='{}'".format(bcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 14")

		if int(lcalories) > 0:
			try:
				cur.execute("UPDATE diary SET lcalories = {} where date ='{}'".format(lcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 15")

		if int(dcalories) > 0:
			try:
				cur.execute("UPDATE diary SET dcalories = {} where date ='{}'".format(dcalories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 16")

		if int(s1calories) > 0:
			try:
				cur.execute("UPDATE diary SET s1calories = {} where date ='{}'".format(s1calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 17")

		if int(s2calories) > 0:
			try:
				cur.execute("UPDATE diary SET s2calories = {} where date ='{}'".format(s2calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 18")

		if int(s3calories) > 0:
			try:
				cur.execute("UPDATE diary SET s3calories = {} where date ='{}'".format(s3calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 19")

		if int(s4calories) > 0:
			try:
				cur.execute("UPDATE diary SET s4calories = {} where date ='{}'".format(s4calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 20")

		if int(s5calories) > 0:
			try:
				cur.execute("UPDATE diary SET s5calories = {} where date ='{}'".format(s5calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 21")

		if int(s6calories) > 0:
			try:
				cur.execute("UPDATE diary SET s6calories = {} where date ='{}'".format(s6calories, datex))
				try:
					conn.commit()
					print("committed")
				except:
					print("commit failed")
			except:
				print("diary error 22")


		try:
			conn.commit()
			print("committed")
		except:
			print("commit diary log 2 failed")


		try:
			cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		except:
			print("diary get failed")
		diary = cur.fetchall()
		conn.close()
		return render_template('diary.html', diary = diary)


		# end
		

	else:
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		try:
			cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		except:
			print("error")
		diary = cur.fetchall()

		conn.close()

		return render_template('updatediarylog.html', diary=diary)

@app.route("/diary", methods=["GET", "POST"])
def diary():
	if request.method == "POST":
		datex = request.form['date']
		weightx = request.form['weight']
		exercisedx = request.form['exercised']
		overatex = request.form['overate']
		breakfastx = request.form['breakfast']
		lunchx = request.form['lunch']
		dinnerx = request.form['dinner']
		snack1x = request.form['snack1']
		snack2x = request.form['snack2']
		snack3x = request.form['snack3']
		snack4x = request.form['snack4']
		snack5x = request.form['snack5']
		snack6x = request.form['snack6']


		# make a list of all the vars I can update

		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()

		# for each option I can update

		# selects all again updated
		cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")

		diary = cur.fetchall()

		conn.close()

		# end
		return render_template('diary.html', diary=diary)

	else:		
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		cur.execute("SELECT date, weight, exercised, overate, breakfast, bcalories, lunch, lcalories, dinner, dcalories, snack1, s1calories, snack2, s2calories, snack3, s3calories, snack4, s4calories, snack5, s5calories, snack6, s6calories, totalcalories FROM diary")
		diary = cur.fetchall()

		#conn.commit()
		conn.close()

		return render_template('diary.html', diary=diary)


	return render_template('diary.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

