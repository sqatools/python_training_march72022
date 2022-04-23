import sqlite3

class DBConnection:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def create_table(self, create_table_query):
        self.conn.execute(create_table_query)
        print("table created successfully")

    def insert_data_to_table(self, insert_query):
        self.conn.execute(insert_query)
        self.conn.commit()
        print("data inserted successfully")

    def get_data_from_table(self, select_query):
        data = self.conn.execute(select_query)
        return data

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    db_name = 'employee.db'
    create_table_query = """CREATE TABLE employee_info
                (ID INT NOT NULL, 
                NAME   TEXT NOT NULL,
                AGE   INT  NOT NULL,
                ADDRESS CHAR(50), 
                EMAIL  CHAR(50));
          """
    insert_query1 = "INSERT INTO employee_info(ID, NAME, AGE, ADDRESS, EMAIL) VALUES(234, 'Abhijeet', 21, 'Mumbai', 'abhijeet@gmail.com');"
    insert_query2 = "INSERT INTO employee_info(ID, NAME, AGE, ADDRESS, EMAIL) VALUES(456, 'Rohit', 24, 'Pune', 'rohit@gmail.com');"
    insert_query3 = "INSERT INTO employee_info(ID, NAME, AGE, ADDRESS, EMAIL) VALUES(323, 'Sherya', 21, 'Delhi', 'shreya@gmail.com');"
    select_query = "select * from employee_info;"
    obj = DBConnection(db_name)
    #obj.create_table(create_table_query)
    #obj.insert_data_to_table(insert_query1)
    #obj.insert_data_to_table(insert_query2)
    #obj.insert_data_to_table(insert_query3)
    data = obj.get_data_from_table(select_query)
    #print(data)

    for row in data:
        #print(row)

        print(f"ID : {row[0]} \n"
              f"Name : {row[1]} \n"
              f"Age : {row[2]} \n"
              f"Address : {row[3]} \n"
              f"Email : {row[4]}")
        print("_"*20)

    obj.close_connection()



