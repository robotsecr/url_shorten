import sqlite3 as sql
db=sql.connect('data.db')
db.execute('''CREATE TABLE IF NOT EXISTS URL(
ID INT PRIMARY KEY NOT NULL,
URL TEXT NOT NULL,
URLSHORTEN NOT NULL) ''')

class shorter_url():
	inst={}
	ids=db.execute('''SELECT ID FROM URL''')
	print(ids)
	try:
		for id_ in ids:
			id=id_[0]
		id=id+1
		
	except:
		id=1
	arrayurl=[]
	counter=id
	def short(self,the_url):
		result=the_url.find(".com")
		if ".com" not in the_url:
			print("Please inter right url")
		else:
			self.inst[the_url]=self.id
			shorting_id=self.encoder(self.id)
			counters=self.id
			self.id=self.id+1
			self.counter=self.counter+1
			data=db.execute(''' SELECT URL FROM URL''')
			
			for rec in data:
				self.arrayurl.append(rec[0])
			if the_url not in self.arrayurl:
				self.thedb(counters,the_url,("url_short.com/"+str(shorting_id)))	
				return "url_short.com/"+str(shorting_id)
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
		db.close()
	def deletefromdb(self):
		delete=db.execute('''DELETE FROM URL WHERE id=9
		''')
		db.commit()
		
shorter=shorter_url()
print("Please Inter your url you want to short:")
data=input("inter:")
print(shorter.short(data))
                                                                 #By Miss.Robot
