import sqlite3 as sq

# to create db--
conn = sq.connect("ex.db")  # creates new if doesn't exist.

# to create a cursor--
cursor = conn.cursor()

# to create table if doesn't exists--
cursor.execute('''CREATE TABLE IF NOT EXISTS people(name TEXT, number INTEGER)''')

#to insert data--
# cursor.execute('''INSERT INTO people VALUES ('Nens', 34454)''') 
# cursor.execute('''INSERT INTO people VALUES ('Heyyy', 324324)''') 
# cursor.execute('''INSERT INTO people VALUES ('asha', 341154)''') 
# cursor.execute('''INSERT INTO people VALUES ('Harsh', 324224)''') 
# cursor.execute('''INSERT INTO people VALUES ('Jone', 34424)''') 
# cursor.execute('''INSERT INTO people VALUES ('Beck', 324924)''') 

#to show data inserted--
print("Using query-->\n")
data=cursor.execute("SELECT * FROM PEOPLE")
for row in data:
    print(row)

#to show data using fetchall--
print("\nUsing fetchall-->\n")
data=cursor.execute("SELECT * FROM PEOPLE")
op=cursor.fetchall()
for newdata in op:
    print(newdata)

#using fetchmany--to limit the fetch data:
#takes 'size' parameter
print("\nUsing fetchmany-->\n")
data=cursor.execute("SELECT * FROM PEOPLE")
op=cursor.fetchmany(5)
for newdata in op:
    print(newdata)

#Read Only one Row:- fetchone()
print("\nUsing fetchone-->\n")
data=cursor.execute("SELECT * FROM PEOPLE")
op=cursor.fetchone()
print(op)


# 'WHERE' CLAUSE TO RETRIEVE DATA----
cursor.execute("SELECT * from people WHERE name Like'H%'")
print("\nfiltered data--->\n")
print(cursor.fetchall())


#update clause to 'update' data----
cursor.execute("UPDATE people SET number =123456 WHERE name = 'Jone'")


print("\nupdated data--->\n")
cursor.execute("SELECT * from people")
print(cursor.fetchall())


# WHERE CLAUSE TO 'DELETE' DATA----
cursor.execute("DELETE from people WHERE name = 'Jone'")
print("\nfiltered data after deletion--->\n")
cursor.execute("SELECT * from people")
print(cursor.fetchall())

#---ORDER BY---

# sql query to display all details from  
# table in 'descending order' based on number. 
cursor = conn.execute("SELECT name from people ORDER BY name DESC") 

print("\nfiltered data after ordering--->\n")
cursor.execute("SELECT name from people")
print(cursor.fetchall())  


#---LIMIT---

# sql query to display 'top4' data from table 
cursor = conn.execute("SELECT * FROM people LIMIT 4") 
print("\nfiltered data after limiting--->\n")
for i in cursor:
    print(i)



#--JOIN---

#executescript-->use to write multiple queries together

#Create and populate tables 
# cursor.executescript(''' 
# CREATE TABLE student( 
# studentID INTEGER NOT NULL, 
# studentName TEXT NOT NULL, 
# PRIMARY KEY(studentID) 
# ); 
  
# CREATE TABLE teacher( 
# teacherID NUMERIC NOT NULL, 
# teacherName TEXT NOT NULL, 
# studentID INTEGER, 
# FOREIGN KEY(studentID) REFERENCES student(studentID), 
# PRIMARY KEY(teacherID) 
# );
                     
# INSERT INTO student(studentID, studentName) VALUES 
# (1,"John Paul"),  
# (2,"Anthony Roy"),  
# (3,"Raj Shetty"), 
# (4,"Sam Reeds"), 
# (5,"Arthur Clintwood"); 
  
# INSERT INTO teacher(teacherID, teacherName, studentID) VALUES 
# (501,"hhh",1), 
# (502,"dnms",1), 
# (503,"dkw",3), 
# (504,"dijwk",2), 
# (505,"djiwk",4), 
# (506,"owow",2), 
# (507,"ekdks",2)                      
#                      ''') 

  
# Query for INNER JOIN 
sql_join = '''SELECT student.studentID, student.studentName, teacher.teacherName
FROM student
INNER JOIN teacher
ON student.studentID = teacher.studentID'''
  
# Executing the query 
cursor.execute(sql_join) 
  
# Fetching rows from the result table 
print("\nfiltered data after join--->\n")
result = cursor.fetchall() 
for row in result: 
    print(row) 

#---DROP---

# cursor.execute('''CREATE TABLE IF NOT EXISTS people2(name TEXT, number INTEGER)''')

# #to insert data--
# cursor.execute('''INSERT INTO people VALUES ('Nens', 34454)''') 
# cursor.execute('''INSERT INTO people VALUES ('Heyyy', 324324)''') 
# cursor.execute('''INSERT INTO people VALUES ('asha', 341154)''') 
# cursor.execute('''INSERT INTO people VALUES ('Harsh', 324224)''') 
# cursor.execute('''INSERT INTO people VALUES ('Jone', 34424)''') 
# cursor.execute('''INSERT INTO people VALUES ('Beck', 324924)''')

# conn.execute("DROP TABLE people2") 
  
# print("\n---data dropped successfully---\n") 


# check if table exists
print('\nCheck if people table exists in the database:-----\n')
listOfTables = cursor.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='people'; """)
 
if listOfTables == []:
    print('Table not found!')
else:
    print('Table found!')


#to count number of changes--00

 
# SQL string to Create a database table
# named person.
create_table = '''CREATE TABLE person(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER NOT NULL
                  );'''
 
# Execute the above SQL query.
conn.execute(create_table)
 
# Print the current total no. of changes.
print("Total changes initially:")
print(f'total_changes = {conn.total_changes}\n')
 
# SQL string to insert records into 
# the table named person.
insert_data = '''INSERT INTO person(name, age)
                  VALUES ("Yogesh",21),
                  ("Vishal", 22),
                  ("Ajit",22),
                  ("Ashish",21);'''
 
# Execute the above SQL query.
conn.execute(insert_data)
 
# Print the current total no. of changes.
print("Total changes after inserting 4 rows:")
print(f'total_changes = {conn.total_changes}\n')
 


# Create a list of column names of the----
# database table named person.
header = [d[0] for d in cursor.description]
 
# Print the column names separated 
# by a single space.
print(*header)
 
# Print the retrieved data.
for row in cursor:
  print(*row)
print()

cursor.close()
conn.close()
