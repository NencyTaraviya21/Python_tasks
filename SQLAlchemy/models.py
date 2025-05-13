from sqlalchemy.orm import sessionmaker         #use to make sessions
from sqlAlchemy_app import Person , engine      #its required to get used in this file

Session = sessionmaker(bind=engine)     #simple use to make session and bind tells where should be making this transactions

session = Session()  #making obj.

person = Person(name='Nency')    #making obj. and to insert data

session.add(person)

session.commit()



