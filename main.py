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
	    print("ERRORRR")
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
		print("heh/")
		try:
			cur = conn.cursor()
		except:
			return "2"
		print("ono")

		#cur.execute("INSERT into calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (?, ?, ?, ?)", (foodname, serving1, serving2, calories1))
	

		#cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
		#	servingsize, servinggrams, caloriesperserving, foodname))

		try:
			cur.execute("UPDATE calorielog set myserving = NULL, mycalories = NULL where myserving is not null")
		except:
			print("Error1")

		try:
			conn.commit()
		except:
			return "4"

		cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving, myserving, mycalories FROM calorielog ORDER BY food")
		calorielog = cur.fetchall()

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

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except:
			print("Error4")


		calorielog = cur.fetchall()
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
			print("heh/")
			try:
				cur = conn.cursor()
			except:
				return "2"
			print("ono")

			#cur.execute("INSERT into calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (?, ?, ?, ?)", (foodname, serving1, serving2, calories1))
			try:
			 	cur.execute("UPDATE calorielog set myserving = '{}', mycalories = (myserving/servinggrams*caloriesperserving) WHERE food = '{}'".format(myserving, foodname))
			#try:
			#	cur.execute(sql)
			except:
				print("Error5")
			print("here")

		

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
		#cur.execute(
		#"SELECT servinggrams, caloriesperserving FROM calorielog WHERE food=?", 
		#("Adobo",))

		cur.execute("SELECT * FROM calorielog ORDER BY food")
		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
			print("hihi")
		except:
			print("Error10")

		#conn.commit()
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

			#cur.execute("INSERT into calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (?, ?, ?, ?)", (foodname, serving1, serving2, calories1))
			#cur.execute("INSERT INTO calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (foodname, serving1, serving2, calories1)")
			#cur.execute('INSERT INTO emp VALUES(%s, %s, %s, %s)',
                                    #(id, name, salary, dept))
			try:
			 	cur.execute("INSERT INTO calorielog VALUES (%s, %s, %s, %s)",
			 	(foodname, serving1, serving2, calories1))
			
			#try:
			#	cur.execute(sql)
			except:
				print("Error11")
			#cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
			#	servingsize, servinggrams, caloriesperserving, foodname))
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
			 	cur.execute("DELETE FROM calorielog WHERE food =" + str(foodnamedel))

			 	#cur.execute("INSERT INTO calorielog VALUES (%s, %s, %s, %s)",
			 	#(foodname, serving1, serving2, calories1))
			#try:
			#	cur.execute(sql)
			except:
				print("Error11")
			#cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
			#	servingsize, servinggrams, caloriesperserving, foodname))
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
		#cur.execute("INSERT into calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (?, ?, ?, ?)", (foodname, serving1, serving2, calories1))

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
		#cur.execute(
		#"SELECT servinggrams, caloriesperserving FROM calorielog WHERE food=?", 
		#("Adobo",))
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

		

		#conn.commit()
		conn.close()



		return render_template('food.html', calorielog=calorielog, mytotalcalories = mytotalcalories)

@app.route("/adddiarylog", methods=["GET", "POST"])

def adddiarylog():

	print("adddiarylog", request.method)


	if request.method == "POST":
		try:
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
			bcalories = request.form['bcalories']
			lcalories = request.form['lcalories']
			dcalories = request.form['dcalories']
			s1calories = request.form['s1calories']
			s2calories = request.form['s2calories']
			s3calories = request.form['s3calories']
			s4calories = request.form['s4calories']
			s5calories = request.form['s5calories']
			s6calories = request.form['s6calories']


			print("ok1")


			try: 
				conn = psycopg2.connect(DATABASE_URL, sslmode='require')
			except:
				return "1"
			print("ok2")
			try:
				cur = conn.cursor()
			except:
				return "2"
			print("ok3")

			



		#update diary set weight = null where date = ('2021-08-08');
			try:	
				# 		cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
			#servingsize, servinggrams, caloriesperserving, foodname))
				cur.execute("INSERT INTO diary (date) VALUES ('{}')".format(datex))
				print("date written")
			except:
				print("diary fail 1")

			if weightx is not NULL:

				try:
					cur.execute("UPDATE diary SET weight = '{}' where date ='{}'".format(weightx, datex))
					print("w")
				except:
					print("diary fail 2")

			if exercisedx is not NULL:
				try:
					cur.execute("UPDATE diary SET exercised = '{}' where date ='{}'".format(exercisedx, datex))
					print("e")

				except:
					print("diary fail 3")

			if overatex is not NULL:
				try:
					cur.execute("UPDATE diary SET overate = {} where date ='{}'".format(overatex, datex))
					print("o")

				except:
					print("diary fail 4")

			if breakfastx is not NULL:
				try:
					cur.execute("UPDATE diary SET breakfast = '{}' where date ='{}'".format(breakfastx, datex))

				except:
					print("diary fail 5")

			if lunchx is not NULL:
				try:
					cur.execute("UPDATE diary SET lunch = '{}' where date ='{}'".format(lunchx, datex))
				except:
					print("diary fail 6")

			if dinnerx is not NULL:
				try:
					cur.execute("UPDATE diary SET dinner = '{}' where date ='{}'".format(dinnerx, datex))
				except:
					print("diary fail 7")

			if snack1x is not NULL:		
				try:
					cur.execute("UPDATE diary SET snack1 = '{}' where date ='{}'".format(snack1x, datex))
				except:
					print("diary fail 8")
			if snack2x is not NULL:
				try:
					cur.execute("UPDATE diary SET snack2 = '{}' where date ='{}'".format(snack2x, datex))
				except:
					print("diary fail 9")

			if snack3x is not NULL:
				try:
					cur.execute("UPDATE diary SET snack3 = '{}' where date ='{}'".format(snack3x, datex))
				except:
					print("diary fail 10")

			if snack4x is not NULL:
				try:
					cur.execute("UPDATE diary SET snack4 = '{}' where date ='{}'".format(snack4x, datex))
				except:
					print("diary fail 11")

			if snack5x is not NULL:
				try:
					cur.execute("UPDATE diary SET snack5 = '{}' where date ='{}'".format(snack5x, datex))
				except:
					print("diary fail 12")

			if snack6x is not NULL:
				try:
					cur.execute("UPDATE diary SET snack6 = '{}' where date ='{}'".format(snack6x, datex))
				except:
					print("diary fail 13")

			if bcalories is not NULL:
				try:
					cur.execute("UPDATE diary SET bcalories = '{}' where date = '{}'".format(bcalories, datex))
				except:
					print("diary fail 14")

			if lcalories is not NULL:
				try:
					cur.execute("UPDATE diary SET lcalories = '{}' where date = '{}'".format(lcalories, datex))
				except:
					print("diary fail 15")

			if dcalories is not NULL:
				try:
					cur.execute("UPDATE diary SET dcalories = '{}' where date = '{}'".format(dcalories, datex))
				except:
					print("diary fail 16")

			if s1calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s1calories = '{}' where date = '{}'".format(s1calories, datex))
				except:
					print("diary fail 17")

			if s2calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s2calories = '{}' where date = '{}'".format(s2calories, datex))
				except:
					print("diary fail 18")

			if s3calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s3calories = '{}' where date = '{}'".format(s3calories, datex))
				except:
					print("diary fail 19")

			if s4calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s4calories = '{}' where date = '{}'".format(s4calories, datex))
				except:
					print("diary fail 20")

			if s5calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s5calories = '{}' where date = '{}'".format(s5calories, datex))
				except:
					print("diary fail 21")

			if s6calories is not NULL:
				try:
					cur.execute("UPDATE diary SET s6calories = '{}' where date = '{}'".format(s6calories, datex))
				except:
					print("diary fail 22")


			print("vars d")
			try:
				conn.commit()
				print("committed")
			except:
				print("commit diary log failed")


				#("INSERT INTO diary (weight, exercised, overate, breakfast, lunch, dinner, snack1, snack2, snack3, snack4, snack5, snack6) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (weightx, exercisedx, overatex, breakfastx, lunchx, dinnerx, snack1x, snack2x, snack3x, snack4x, snack5x, snack6x))
			#except:
				#print("fail")
				#else:
					#print("else")
					#pass

			#print("ok4")

			print("Finis!")
			try:
				cur.execute("SELECT * FROM diary")
			except:
				print("diary get failed")
			#cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
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
		#cur.execute(
		#"SELECT servinggrams, caloriesperserving FROM calorielog WHERE food=?", 
		#("Adobo",))
		cur.execute("SELECT * FROM diary")
		#cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
		diary = cur.fetchall()
		print("boo")

		#conn.commit()
		conn.close()

		return render_template('adddiarylog.html', diary=diary)

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

		print("ahh")
		# selects all again updated
		cur.execute("SELECT * FROM diary")
		#cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")

		diary = cur.fetchall()

		conn.close()

		# end
		return render_template('diary.html', diary=diary)

	else:		
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		cur = conn.cursor()
		#cur.execute(
		#"SELECT servinggrams, caloriesperserving FROM calorielog WHERE food=?", 
		#("Adobo",))
		cur.execute("SELECT * FROM diary")
		#cur.execute("SELECT date, max(weight), exercised, overate, max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
		diary = cur.fetchall()
		print("boo")

		#conn.commit()
		conn.close()

		return render_template('diary.html', diary=diary)


	return render_template('diary.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

