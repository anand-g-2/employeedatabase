import psycopg2 as pg2
class StaffDataBase(object):
    def create_db(self):
        # Create a new database for employees(staff), if it
        # does not exist already
        conn = pg2.connect(
            user='postgres', password='password',
            host='127.0.0.1', port= '5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        sqlCreateDatabase = '''SELECT 'CREATE DATABASE staff'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'staff')'''
        cursor.execute(sqlCreateDatabase)
        conn.close()

    def create_table(self):
        # Connect to the employees(staff) database and create
        # a table, if it does not exist already
        conn = pg2.connect(
            database='staff',user='postgres', password='password',
            host='127.0.0.1', port= '5432'
            )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS stafftable(
            S_No SERIAL PRIMARY KEY,
            Staff_Id VARCHAR(10) UNIQUE NOT NULL,
            Staff_Name VARCHAR(50) NOT NULL,
            Department_Name VARCHAR(30) NOT NULL,
            Email_Id VARCHAR(30) UNIQUE NOT NULL,
            Contact_No VARCHAR(15))'''
            )

    def __init__(self):
        # initialize the paramters in the table
        self.StaffId = " "
        self.StaffName = " "
        self.DeptName = " "
        self.EmailId =  " "
        self.ContactNo = " "
        
    def give_items(self):
        # get the values for the employee paramters to be
        # updated to the table
        self.StaffId = input("Enter Staff ID: ")
        self.StaffName = input("Enter Staff Name: ")
        self.DeptName = input("Ennter Department Name: ")
        self.EmailId = input("Enter Email Id: ")
        self.ContactNo = str(input("Enter Contact Number: "))
        return self.StaffId, self.StaffName, self.DeptName, self.EmailId, self.ContactNo
    def del_items(self):
        self.StaffId = input("Enter Staff Id: ")
        return self.StaffId
                            
    
