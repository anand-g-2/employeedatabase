import psycopg2 as pg2
import pandas as pd
from staffdata import StaffDataBase

staff = StaffDataBase()
staff.create_db()
staff.create_table()
conn = pg2.connect(
   database="staff", user='postgres', password='password',
   host='127.0.0.1', port= '5432'
)
conn.autocommit = True

with conn:
    print("connection created to database")
    cur = conn.cursor()
    choice = 'y'
    while(choice == 'y'):
        print("1. Add New Staff \n2. Display Staff Table \n3. Delete Staff Entry \n4. Close Connection")
        response = int(input("Enter your choice: "))
        
        if(response == 1):
            (staffid,name,deptname,email,contactno) = staff.give_items()
            print(name)
            cur.execute(
                '''INSERT INTO stafftable (Staff_Id,Staff_Name,Department_Name,Email_Id,Contact_No)
                   VALUES(%s,%s,%s,%s,%s)''',(staffid,name,deptname,email,contactno)
                )
            conn.commit()
            msg = "Contact Successfully Added!"

        elif(response == 2):
            cur.execute(
                '''SELECT * FROM stafftable'''
                )
            result = cur.fetchall()
            df = pd.DataFrame(result,columns=['S_No','Staff_Id','Staff_Name',
                                              'Department_Name','Email_Id',
                                              'Contact_No'])
            print(df)

        elif(response == 3):
            StaffId = staff.del_items()
            data=(StaffId, )
            query='''DELETE FROM stafftable WHERE Staff_Id = (%s)'''
            cur.execute(query,data)
            conn.commit()

        elif(response == 4):
            print("connection to database is closed")
            break
        
        else:
            print("Please Check Your Response")
            choice = input("Press 'y' tp continue: ")
            
        
        
        
