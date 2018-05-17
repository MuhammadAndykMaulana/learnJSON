class Student:
 
	def __init__(self,name,email,contact,skills,ug=None,pg=None):
 
        	self.email=email
	        self.contact=contact
        	self.name=name
	        self.skills=[skills]
 
        	self.edu={"ug":[ug],"pg":[pg]} 

james=[Student("James","j@j.com","+1 7789990007","Python","CS", "CS"),
       Student("Jordan","jordan@j.com","+1 7789990007","Python","CS", "CS")]
print vars(james)
