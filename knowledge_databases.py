from knowledge_model import Base, animals

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_animal(name, gender, finished_lab):
	animal_object = animals(
		name=name,
		gender=gender,
		finished_lab=finished_lab)
	session.add(animal_object)
	session.commit()

add_animal("cat", "F", True)
add_animal("sheep", "F", True)
add_animal("elephant", "M", True)

def query_all_animal():
	animal = session.query(animals).all()
	return animal

print(query_all_animal())
	
def query_animal_by_topic(the_name):
	animal = session.query(animals).filter_by(name=the_name).first()
	return animal
	
print(query_animal_by_topic("sheep"))

def delete_animal_by_topic(name):
	session.query(animals).filter_by(name=name).delete()
	session.commit()

delete_animal_by_topic("elephant")

def query_animal_by_topic(the_name):
	animal = session.query(animals).filter_by(name=the_name).first()
	return animal
	
print(query_animal_by_topic("elephant"))
	
def delete_all_animal():
	session.query(animals).delete()
	session.commit()

print(delete_all_animal())

add_animal("cat", "F", True)
add_animal("sheep", "F", True)
add_animal("elephant", "M", True)

def edit_animal_gender(name,gender):
	animal_object = session.query(animals).filter_by(name=name).first()
	animal_object.gender=gender
	session.commit()

edit_animal_gender("cat","M")
	



