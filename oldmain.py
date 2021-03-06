from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import mariadb


mytotalcalories = 0

def get_db_connection():
	try:
	# change this to your settings
	    conn = mariadb.connect(
	        user="root",
	        password="password",
	        host="localhost",
	        port=3306,
	        database="calories"
	    )
	    return conn
	except mariadb.Error as e:
	    print(f"Error connecting to MariaDB Platform: {e}")
	    sys.exit(1)



app = Flask(__name__)

@app.route("/")
def index():

	return render_template('index.html')


@app.route("/calcclear", methods=["GET", "POST"])
def calcclear():
	if request.method == "POST":

		try: 
			conn = get_db_connection()
		except:
			return "1"
		try:
			cur = conn.cursor()
		except:
			return "2"


		try:
			cur.execute("UPDATE calorielog set myserving = NULL, mycalories = NULL where myserving is not null")
		except mariadb.Error as e:
			print(f"Error: {e}")

		try:
			conn.commit()
		except:
			return "4"

		cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving, myserving, mycalories FROM calorielog")
		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except mariadb.Error as e:
			print(f"Error: {e}")


		conn.close()
		return render_template('calccal.html', calorielog = calorielog, mytotalcalories = mytotalcalories)



	else:
		try:
			cur.execute("SELECT * FROM calorielog")
		except mariadb.Error as e:
			print(f"Error: {e}")

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except mariadb.Error as e:
			print(f"Error: {e}")


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
				conn = get_db_connection()
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"

			try:
			 	cur.execute("UPDATE calorielog set myserving = '{}', mycalories = (myserving/servinggrams*caloriesperserving) WHERE food = '{}'".format(myserving, foodname))
			except mariadb.Error as e:
				print(f"Error: {e}")

		

			try:
				conn.commit()
			except mariadb.Error as e:
				print(f"Error: {e}")



			try:
				cur.execute("SELECT * FROM calorielog")
			except mariadb.Error as e:
				print(f"Error: {e}")


			calorielog = cur.fetchall()

			try:
				cur.execute("SELECT sum(mycalories) FROM calorielog")
				mytotalcalories = cur.fetchone()[0]
			except mariadb.Error as e:
				print(f"Error: {e}")

			conn.close()

			return render_template('calccal.html', calorielog = calorielog, mytotalcalories = mytotalcalories)


		except mariadb.Error as e:
			print(f"Error: {e}")
			return "Database Connection Error"
			return render_template('calccal.html')

	else:
		conn = get_db_connection()
		cur = conn.cursor()

		cur.execute("SELECT * FROM calorielog")
		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except mariadb.Error as e:
			print(f"Error: {e}")

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
			myserving = request.form['myserving']

			try: 
				conn = get_db_connection()
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"

			try:
			 	cur.execute("INSERT INTO calorielog (food, servingsize, servinggrams, caloriesperserving) VALUES (?, ?, ?, ?)", (foodname, serving1, serving2, calories1))
			
			except mariadb.Error as e:
				print(f"Error: {e}")
			try:
				conn.commit()
			except:
				return "4"

			cur.execute("SELECT food, servingsize, servinggrams, caloriesperserving, mycalories FROM calorielog")
			calorielog = cur.fetchall()
			conn.close()
			return render_template('food.html', calorielog = calorielog)


		# end
		except:
			return "Database Connection Error"
			return render_template('addfood.html')

	else:
		return render_template('addfood.html')



@app.route("/food", methods=["GET", "POST"])
def food():
	if request.method == "POST":
		foodname = request.form['foodname']
		serving1 = request.form['serving1']
		serving2 = request.form['serving2']
		calories1 = request.form['calories1']
		myserving = request.form['myserving']

		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("UPDATE calorielog set servingsize, servinggrams, caloriesperserving = '{}, {}, {}' where foodname = '{}'".format(
			servingsize, servinggrams, caloriesperserving, foodname))
		# selects all again updated
		cur.execute("SELECT * FROM calorielog")

		calorielog = cur.fetchall()

		conn.close()

		return render_template('food.html', calorielog=calorielog)

	else:		
		conn = get_db_connection()
		cur = conn.cursor()


		cur.execute("SELECT * FROM calorielog")
		calorielog = cur.fetchall()

		try:
			cur.execute("SELECT sum(mycalories) FROM calorielog")
			mytotalcalories = cur.fetchone()[0]
		except mariadb.Error as e:
			print(f"Error: {e}")

		
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




			try: 
				conn = get_db_connection()
			except:
				return "1"
			try:
				cur = conn.cursor()
			except:
				return "2"

			if not weightx:
				weightx = 0

			if not exercisedx:
				exercisedx = 0

			if not overatex:
				overatex = 0

			if not bcalories:
				bcalories = 0

			if not lcalories:
				lcalories = 0

			if not dcalories:
				dcalories = 0

			if not s1calories:
				s1calories = 0

			if not s2calories:
				s2calories = 0

			if not s3calories:
				s3calories = 0

			if not s4calories:
				s4calories = 0

			if not s5calories:
				s5calories = 0

			if not s6calories:
				s6calories = 0








			try:	
				cur.execute("INSERT INTO diary (date) VALUES ('{}')".format(datex))
				print("date written")
				cur.execute("UPDATE diary SET weight = '{}' where date ='{}'".format(weightx, datex))
				print("w")

				cur.execute("UPDATE diary SET exercised = '{}' where date ='{}'".format(exercisedx, datex))
				print("e")
				cur.execute("UPDATE diary SET overate = {} where date ='{}'".format(overatex, datex))
				print("o")
				cur.execute("UPDATE diary SET breakfast = '{}' where date ='{}'".format(breakfastx, datex))
				cur.execute("UPDATE diary SET lunch = '{}' where date ='{}'".format(lunchx, datex))
				cur.execute("UPDATE diary SET dinner = '{}' where date ='{}'".format(dinnerx, datex))
				cur.execute("UPDATE diary SET snack1 = '{}' where date ='{}'".format(snack1x, datex))
				cur.execute("UPDATE diary SET snack2 = '{}' where date ='{}'".format(snack2x, datex))
				cur.execute("UPDATE diary SET snack3 = '{}' where date ='{}'".format(snack3x, datex))
				cur.execute("UPDATE diary SET snack4 = '{}' where date ='{}'".format(snack4x, datex))
				cur.execute("UPDATE diary SET snack5 = '{}' where date ='{}'".format(snack5x, datex))
				cur.execute("UPDATE diary SET snack6 = '{}' where date ='{}'".format(snack6x, datex))

				cur.execute("UPDATE diary SET bcalories = '{}' where date = '{}'".format(bcalories, datex))
				cur.execute("UPDATE diary SET lcalories = '{}' where date = '{}'".format(lcalories, datex))
				cur.execute("UPDATE diary SET dcalories = '{}' where date = '{}'".format(dcalories, datex))
				cur.execute("UPDATE diary SET s1calories = '{}' where date = '{}'".format(s1calories, datex))
				cur.execute("UPDATE diary SET s2calories = '{}' where date = '{}'".format(s2calories, datex))
				cur.execute("UPDATE diary SET s3calories = '{}' where date = '{}'".format(s3calories, datex))
				cur.execute("UPDATE diary SET s4calories = '{}' where date = '{}'".format(s4calories, datex))
				cur.execute("UPDATE diary SET s5calories = '{}' where date = '{}'".format(s5calories, datex))
				cur.execute("UPDATE diary SET s6calories = '{}' where date = '{}'".format(s6calories, datex))


				conn.commit()


			except mariadb.Error as e:
				print("fail")
				print(f"Error: {e}")
	



			cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
			diary = cur.fetchall()
			conn.close()
			return render_template('diary.html', diary = diary)


		# end
		except:
			return "Database Connection Error"
			return render_template('adddiarylog.html')

	else:
		conn = get_db_connection()
		cur = conn.cursor()

		cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
		diary = cur.fetchall()

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



		conn = get_db_connection()
		cur = conn.cursor()



		cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")

		diary = cur.fetchall()

		conn.close()

		return render_template('diary.html', diary=diary)

	else:		
		conn = get_db_connection()
		cur = conn.cursor()


		cur.execute("SELECT date, max(weight), max(exercised), max(overate), max(breakfast), max(bcalories), max(lunch), max(lcalories), max(dinner), max(dcalories), max(snack1), max(s1calories), max(snack2), max(s2calories), max(snack3), max(s3calories), max(snack4), max(s4calories), max(snack5), max(s5calories), max(snack6), max(s6calories) FROM diary group by date ORDER BY date desc")
		diary = cur.fetchall()
		print("boo")

		conn.close()

		return render_template('diary.html', diary=diary)


	return render_template('diary.html')

if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)



