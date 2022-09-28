Employee Database 

This code is used to create a database for maintaining employee details. The code also provides options to display the table as well as to delete entries from the table.

The code is comprised of two files. The first file staffdata.py has a class StaffDatabase() with the following five functions:
       create_db(): Create a new database for employees(staff), if it does not exist already
       create_table(): Connect to the employees(staff) database and createa table, if it does not exist already
       __init__(): Initialize the parameters in the table
       give_items(): get the employee parameters to be inserted into the table
       del_tems(): get the ID of the staff whose entry has to be removed

The scond file stafftable.py gets the table as well as the required data from the StaffDatabase() class in the first file and then updates the table accordingly.
This code allows four different operations to be performed on the table:
1. Add New Staff
2. Display Staff Table
3. Delete Staff Entry
4. Close Connection




