import sqlite3

conn = sqlite3.connect('student.db')

#print("Operation is Successful")

"""
conn.execute('''CREATE TABLE student_info
                (ID INT NOT NULL, 
                 NAME   TEXT NOT NULL,
                AGE   INT  NOT NULL,
                ADDRESS CHAR(50), 
                EMAIL  CHAR(50));
''')

print("Table is created Successfully")
"""

# Insert data to the table
"""
conn.execute("INSERT INTO student_info(ID, NAME, AGE, ADDRESS, EMAIL) VALUES(234, 'Rohit', 25, 'Pune', 'rohit@gmail.com');")

conn.commit()

print("Record inserted successfully")
"""

data = conn.execute("select * from student_info");

print(data)

for row in data:
    print(row)

conn.close()





