import sqlite3


def dataentry():
	con=sqlite3.connect('dataform.db')
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS dataform(id INTEGER PRIMARY KEY,enuser text, enfirstname text,enlastname text)")
	con.commit()
	con.close()
	
	
def  adddata(enuser,enfirstname,enlastname):
	con=sqlite3.connect('dataform.db')
	cur=con.cursor()
	cur.execute("INSERT INTO dataform VALUES(NULL,?,?,?)",(enuser,enfirstname,enlastname))
	con.commit()
	con.close()
	
	

