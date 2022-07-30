import psycopg2

# Database connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='127.0.0.1', port= '5432'
)
# Using the cursor() method we are creating cursor object
cursor = conn.cursor()
conn.autocommit = True

#Droping tables if already exists.
cursor.execute("DROP TABLE IF EXISTS Customer")
cursor.execute("DROP TABLE IF EXISTS Transactions")

#Creating tables as per requirement
table_queries =(
    '''CREATE TABLE Customer (
       customer_id INTEGER PRIMARY KEY,
       first_name VARCHAR(20),
       last_name VARCHAR(20),
       date_of_birth TIMESTAMP
    )''',
    '''CREATE TABLE Transactions (
       txn_id INTEGER PRIMARY KEY,
       customer_id INTEGER REFERENCES Customer(customer_id),
       txn_type VARCHAR(10) CHECK(txn_type IN ('CREDIT', 'DEBIT')),
       txn_amount INTEGER,
       transaction_date DATE
    )'''
)

for query in table_queries:
    cursor.execute(query)
print("Tables created successfully........")
conn.commit()
conn.close()
