Dependencies: Flask, sqlite3, csv. (latter two should be installed by default but just in case)


How to run (after installing dependencies):

1. Run dbsetup.py to build and and populate the database (will create a file in the same directory called 'shop.db')
2. run API.py to start the API, and go to http://127.0.0.1:5000/customer/x in a browser, where 'x' is the customer_id of the customer you want returned.
3. run csv export.py, which will save a  called 'data.csv' with the results to the same directory that contains csv export.py. Open the csv to view results.

Reasoning:

For the database, I used sqlite3 as it is inbuilt in Python by default, doesn't require any separate server setup, and is quick and simple to work with for a small database and dataset such as this.

For the API, I used Flask. This was done for similar reasons as the above, in that Flask is lightweight and easy to work with for such a small API endpoint. 
Additionally, I have some prior experience with Flask as I used it for a couple of projects during my degree.

CSV handling is built into Python by default with the csv library, so I used the writer function of that to write each object from the database to the file.

Additionally, when pulling data from the database to be written for the CSV, 
I decided to join the customer and their orders via the SQL query rather than doing it separately. 
Doing it separately would involve less complex SQL queries and so less room for error, but it would add 1-2 extra steps to the process. 
As this is a simple set of data and simple output, I decided to implement the former for efficiency since there isn't much that could go wrong with the data.

Application Flow:

When the database is being created, the list of lists 'customers' is looped through, with each item being added as a new entry in the 'customers' table, with the fields of each entry being filled with the items within each customer list. 
Once this is finished, the same thing happens with the 'orders' list. The data is then commited to the database and saved.

When the API file is run, the API is established using Flask and waits for an HTTP request. When a request is passed through, the API checks the request's route definition.
assuming the request is correct, it then connects to the database and searches through the customers table for an item with the customer_id matching the number at the end of the request. 
If one exists, it retrieves it, then queries the orders table for all items connected to that customer via foreign key. These database rows are then converted to JSOn and returned to the client and displayed.

In the csv export script, an SQL query is run that searches the customers table for all customers where their status = 'active'. It then uses JOIN to combine each customer with their orders from the orders table.
This results in a series of customer rows. fetchall() then returns all of these rows as a list of tuples, wher 1 tuple = 1 row. With the extracting complete, the CSV file is then opened.
The initial row is written to the CSV to act as column headers. It then loops through each row retrieved from the database, and combines the firstname + lastname fields, as well as calculating a total cost for their orders. Each individual new row is then written in the CSV.

Improvements for the future:

If this were a larger project to be expanded on in the future, I would likely combine the functions of the API and the CSV export file. The API would be expanded to allow searching for more than one user at a time, as well as searching by properties other than just user ID.
The data returned by the API would then be saved to a CSV. This would remove the already slightly redundant CSV return file, as well as allow data from the database to be saved to a file remotely via the API, instead of requiring direct access to the DB.

Additionally, if this project was to be expanded on, I'd consider moving the database from sqlite3 to something like SQL Server. While more complex, SQL Server is more robust and better for handling large amounts of data,
as well as more secure and easier to perform database management with, via external software.

I would also add more fields to the customer and order data to ensure better record keeping, for example the date customers were added to the system, or the date an order was made.