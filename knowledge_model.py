from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class animals(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

   __tablename__ = 'animals'
   animal_id = Column(Integer, primary_key=True)
   name = Column(String)
   gender = Column(Integer)
   finished_lab = Column(Boolean)

   def __repr__(self):
   	return ("animal name: {}\n"
   			"animal gender: {}\n"
   			"lab status: {}").format (
   				self.name,
   				self.gender,
   				self.finished_lab)

x = animals(name="dog", gender="m")
print (x)
