import sqlite3
import datetime

class Model:

	  def __init__(self):
	    self.history_dict=[]
	    self.db_status=True
	    self.conn=None
	    self.cur=None
	    try:
	      self.conn=sqlite3.connect("income_tax_db")
	      print("connected")
	      self.cur=self.conn.cursor()
	      print("cursor opened")
	    except  sqlite3.DatabaseError as ex:
	        print("DB Error",ex)
	        self.db_status=False
	    self.history_dict=[]
	    

	  def get_db_status(self):
	    return self.db_status

	  def user_update(self,user):
	  	self.cur.execute("drop table if exists user")
	  	self.cur.execute("CREATE TABLE if not exists user(id text,user text)")
	  	self.cur.execute("INSERT INTO user VALUES('1',:1)",(user,))
	  	self.conn.commit()	     

	  def get_user(self):
	    try:
	      self.cur.execute("SELECT * from user where id='1'")
	      user=self.cur.fetchone()
	      self.conn.commit()
	      usern=user[1]
	      return usern
	    except Exception as ex:
	      print("DB Error:",ex)
	      return "Username Neeraj"


	  def date_time(self):
	    today=datetime.datetime.now()
	    time=str(today.year)
	    for i in (today.month,today.day,today.hour,today.minute,today.second):
	      if i<=9:
	        time+='0'+str(i)
	      else:
	        time+=str(i)
	    print(time)
	    return time


	  def close_db_connection(self):
	    if self.cur is not None:
	        self.cur.close()
	        print("cursor closed")
	    if self.conn is not None:
	        self.conn.close()
	        print("connection closed")


	  def search_user(self,user):
	    try:
	      self.cur.execute("SELECT * from INCOME_ID where user=:1",(user,))
	      user_tuple=self.cur.fetchone()
	      if user_tuple is None:
	        return False
	      else:
	        return True
	    except sqlite3.DatabaseError as ex:
	      print("DB error",ex)
	      self.cur.execute("CREATE TABLE INCOME_ID (first text,last text,user text,pass text,pan text,mob integer,dob integer,ques text,ans text)")
	      self.cur.execute("CREATE TABLE history(user Text,name TEXT,pan TEXT,age INTEGER,year TEXT,gross_salary INTEGER,exemption_from_salary INTEGER,income_from_interest INTEGER,other_income INTEGER,interest_paid_on_home_loan INTEGER,rental_income_received INTEGER,interest_paid_on_loan INTEGER,c80 INTEGER,tta80 INTEGER,d80 INTEGER,g80 INTEGER,e80 INTEGER,eea80 INTEGER,ccd80 INTEGER,total_income INTEGER,deductions INTEGER,gross_total_income INTEGER,payable_income_tax INTEGER,time_date TEXT)")
	      self.conn.commit()
	      print("table CREATE successfully")
	      return False

	  def find_user(self,mob):
	  	try:
	  		self.cur.execute("SELECT user from INCOME_ID where mob=:1",(mob,))
	  		user_tuple=self.cur.fetchone()
	  		return user_tuple
	  	except Exception as ex:
	  		print("user not find",ex)
	  		return None

	  def search_mob(self,mob):
	    self.cur.execute("SELECT * from INCOME_ID where mob=:1",(mob,))
	    mob_tuple=self.cur.fetchone()
	    if mob_tuple is None:
	      return False
	    else:
	      return True

	  def search_pan(self,pan):
	    self.cur.execute("SELECT * from INCOME_ID where pan=:1",(pan,))
	    pan_tuple=self.cur.fetchone()
	    if pan_tuple is None:
	      return False
	    else:
	      return True

	  def ragistration(self,first,last,user,passw,pan,mob,dob,ques,ans):
	    if self.search_user(user) == True:
	      return"user already ragistrat"
	    elif self.search_mob(mob)==True:
	      return"mob already ragistrat"
	    elif self.search_pan(pan) ==True:
	      return"pan already ragistrat"
	    else:
	      self.cur.execute("INSERT INTO INCOME_ID VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9)",(first,last,user,passw,pan,mob,dob,ques,ans))
	      self.conn.commit()
	      return 'successfull'

	  def log_in(self,user,passw):
	    self.search_user(user)
	    self.cur.execute("SELECT pass from INCOME_ID where user=:1",(user,))
	    user_tuple=self.cur.fetchone()
	    if user_tuple==None:
	      return False,"Please enter valid user name"
	    elif user_tuple ==(passw,):
	      return True,"login successful"
	    else :
	      return False,"Please enter valid password"

	  def add_history(self,user,name,pan,age,year,gross_salary,exemption_from_salary,income_from_interest,other_income,interest_paid_on_home_loan,rental_income_received,interest_paid_on_loan,c80,att80,d80,g80,e80,eea80,ccd80,total_income,deductions,gross_total_income,payable_income_tax):
	    time_date=self.date_time()
	    self.cur.execute("INSERT INTO history VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24)",(user,name,pan,age,year,gross_salary,exemption_from_salary,income_from_interest,other_income,interest_paid_on_home_loan,rental_income_received,interest_paid_on_loan,c80,att80,d80,g80,e80,eea80,ccd80,total_income,deductions,gross_total_income,payable_income_tax,time_date))
	    self.conn.commit()
	    print("database successfully save")

	  def remove_history(self,user,time_date):
	    self.cur.execute("DELETE FROM history where user=:1 and time_date=:2",(user,time_date))
	    self.conn.commit()
	    print("select data successfully remove")

	  def get_history(self,user):
	    self.cur.execute("SELECT name,pan,age,gross_total_income,payable_income_tax,time_date from history where user=:1",(user,))
	    history_present=False
	    for i in self.cur:
	    	self.history_dict.append(i)
	    	history_present=True

	    if history_present==True:
	    	return self.history_dict
	    else:
	    	return history_present


	  def get_all_history(self,user,time):
	  	self.cur.execute("SELECT * from history where user=:1 and time_date=:2",(user,time))
	  	h=self.cur.fetchall()
	  	return h[0]

	  def update_mob(self,user,mob):
	    self.cur.execute("UPDATE INCOME_ID set mob=:1 where user=:2",(mob,user))
	    self.conn.commit()

	  def update_pass(self,user,passw):
	    self.cur.execute("UPDATE INCOME_ID set pass=:1 where user=:2",(passw,user))
	    self.conn.commit()

	  def update_ques(self,user,ques):
	    self.cur.execute("UPDATE INCOME_ID set ques=:1 where user=:2",(ques,user))
	    self.conn.commit()

	  def update_ans(self,user,ans):
	    self.cur.execute("UPDATE INCOME_ID set ans=:1 where user=:2",(ans,user))
	    self.conn.commit()

	  def get_ques_pan(self,user):
	    self.cur.execute("SELECT ques,ans,pan from INCOME_ID where user=:1",(user,))
	    user=self.cur.fetchone()
	    return user

	  def get_pass(self,user):
	   	self.cur.execute("SELECT pass from INCOME_ID where user=:1",(user,))
	   	user=self.cur.fetchone()
	   	return user[0]

	  def get_mob(self,user):
	   	self.cur.execute("SELECT mob from INCOME_ID where user=:1",(user,))
	   	user=self.cur.fetchone()
	   	return user[0]

	  def get_ques(self,user):
	   	self.cur.execute("SELECT ques from INCOME_ID where user=:1",(user,))
	   	user=self.cur.fetchone()
	   	return user[0]

	    


obj=Model()
#obj.ragistration('Neeraj','Khajuriya','neeraj7071','nk123456','BHJ5782GH6',7071750746,25071999,3,'balmandir')
#obj.get_id(7071750746)
obj.close_db_connection()