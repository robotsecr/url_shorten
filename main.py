import sqlite3 as sql
from flask import Flask,request
app=Flask(__name__)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
db=sql.connect('data.db',check_same_thread=False)
db.execute('''CREATE TABLE IF NOT EXISTS URL(
ID INT PRIMARY KEY NOT NULL,
URL TEXT NOT NULL,
URLSHORTEN NOT NULL) ''')

class shorter_url():
	inst={}
	def checkid(self):
		ids=db.execute('''SELECT ID FROM URL''')
		print(ids)
		try:
			for id_ in ids:
				id=id_[0]
			id=id+1
		
		except:
			id=1
		return id
	arrayurl=[]
	def short(self,the_url):
		if ".com" not in the_url:
			return "error sorry"
		else:
			self.inst[the_url]=self.checkid()
			shorting_id=self.encoder(self.checkid())
			counters=self.checkid()
			data=db.execute(''' SELECT URL FROM URL''')
			for rec in data:
				self.arrayurl.append(rec[0])
			if the_url not in self.arrayurl:
				self.thedb(counters,the_url,("joly.com/"+str(shorting_id)))
				return "joly.com/"+str(shorting_id)
					
				
			else:
				URL=db.execute('''SELECT URLSHORTEN FROM URL WHERE URL=?''',(the_url,))
				for url in URL:
					the_url=url[0]
				return the_url
	def encoder(self,id):
		base10='0123456789'
		ret=[]
		while id>0:
			val=id%len(base10)
			ret.append(base10[val])
			id=id//len(base10)
		
		return "".join(ret[::-1])
	def thedb(self,id,url,shorten_url):
		insert=db.execute('''INSERT INTO URL(ID,URL,URLSHORTEN)
		VALUES(?,?,?)
		''',(id,url,shorten_url))
		db.commit()
	def deletefromdb(self):
		delete=db.execute('''DELETE FROM URL WHERE id=9
		''')
		
		
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.route("/",methods=["Get","POST"])
def input():
	error=""
	checker=0
	the_shorten=""
	shorter=shorter_url()
	if request.method =="POST":
		url=request.form["url"]
		test=shorter.short(str(url))
		if "error" in test:
			error+="<p> {!r} is not a valid url".format(request.form["url"])
			checker=1
		else:
			the_shorten=shorter.short(url)	
			checker=2
	if checker==1:
		return '''
			<! doctype html><html>
			<head>
			<title>Home</title>
			</head>
			<body>
			{errors}
			<form method="post" action=".">
			<p><input name="url"/></p>
			<p><input type="submit" value="Do The Shorten">
			</p>
			</form>
			</body>
			</html>'''.format(errors=error)
	else:
		return '''
			<! doctype html><html>
			<head>
			<title>Home</title>
			</head>
			<body>
			<form method="post" action=".">
			<p><input name="url"/></p>
			<p><input type="submit" value="Do The Shorten">
			</p>
			</form>
			{url_shorten}
			</body>
			</html>'''.format(url_shorten=the_shorten)
if __name__=='__main__':
	app.run(debug=True,port=90)

                                                                  #By Miss.Robot
