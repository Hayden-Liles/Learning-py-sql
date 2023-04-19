import mysql.connector

# Connect to MySQL database server
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="password",
    # NOTE choosing which DB to connec to
    database="pytest"
)

mc = db.cursor()

# SECTION ________________


# NOTE CREATE TABLE
# mc.execute("""
# CREATE TABLE
# customers
# (
# id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
# name VARCHAR(255),
# address VARCHAR(255)
# )
# """)

# SECTION ________________


# NOTE DROP TABLE
# mc.execute("""
# DROP TABLE
# customers
# """)

# SECTION ________________


# NOTE ALTER TABLE
# mc.execute("""
# ALTER TABLE
# customers
# ADD COLUMN
# id INT AUTO_INCREMENT PRIMARY KEY
# """)

# SECTION ________________

# NOTE INSERT INTO TABLE customers
# NOTE %s is a placeholder
# sql = """
# INSERT
# INTO customers
# (name, address)
# VALUES
# (%s, %s)
# """

# val = ("John", "Highway 21")
# mc.execute(sql, val)
# db.commit()


# SECTION ___________


# NOTE You're able to execute many sql statements
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# mc.executemany(sql, val)

# NOTE commit() is what saves data to the db
# db.commit()

# SECTION _______________

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mc.execute(sql, val)

# db.commit()
# NOTE                               VVV Last id inserted
# print("1 record inserted, ID:", mc.lastrowid)

# SECTION ________________

# NOTE fetchall() method, which fetches all rows from the last executed statement.
# mc.execute("""
#     SELECT
#     *
#     FROM
#     customers
# """)

# myresult = mc.fetchall()

# for x in myresult:
#     print(x)

# SECTION ________________ SELECT ... FROM

# mc.execute("""
# SELECT
# address
# FROM
# customers
# """)

# myresult = mc.fetchall()

# for x in myresult:
#     print(x)

# SECTION ________________ SELECT ONE

# mc.execute("""
# SELECT
# *
# FROM
# customers
# """)

# myresult = mc.fetchone()
# print(myresult)

# SECTION ________________ SELECT ... FROM WHERE

# sql = """
# SELECT
# *
# FROM
# customers
# WHERE
# address = 'Park Lane 38'
# """

# mc.execute(sql)
# myresule = mc.fetchall()
# for x in myresule:
#     print(x)

# SECTION ________________ Use the %  to represent wildcard characters: AKA HAS 'way' in it VVVV

# sql = """
# SELECT
# *
# FROM
# customers
# WHERE address LIKE '%way%'
# """
# mc.execute(sql)
# res = mc.fetchall()
# for x in res:
#     print(x)


# SECTION ________________ ONCE AGAIN USING PLACEHOLDER to prevent sql injection

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mc.execute(sql, adr)

# myresult = mc.fetchall()

# for x in myresult:
#     print(x)

# SECTION ________________ ORDER BY
# NOTE ACCENDING By default
# sql = """
# SELECT *
# FROM
# customers
# ORDER BY name
# """
# NOTE TO DO DECSENDING
# sql = """
# SELECT *
# FROM customers
# ORDER BY
# name DESC
# """

# mc.execute(sql)
# res = mc.fetchall()
# for x in res:
#     print(x)

# SECTION __________ DELETE
# sql = """
# DELETE FROM
# customers
# WHERE
# address = 'Mountain 21'
# """
# mc.execute(sql)
# db.commit()
# print(mc.rowcount, "rows deleted")

# NOTE USING THE PLACEHOLDER VVVV
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mc.execute(sql, adr)
# db.commit()
# print(mc.rowcount, "rows deleted")

# SECTION __________ DROP TABLE

# sql = """
# DROP TABLE
# customers
# """
# mc.execute(sql)

# NOTE ONLY IF IT EXISTS VVV

# sql = """
# DROP TABLE
# IF EXISTS
# customers
# """
# mc.execute(sql)

# SECTION ___________ UPDATE A TABLE

# sql = """
# UPDATE
# customers
# SET
# NOTE  SET IT TO  VVV  | WHERE VVV    ==  VVV
# address = 'Canyon 123' WHERE address = 'Valley 345'
# """
# mc.execute(sql)
# db.commit()

# print(mc.rowcount, "rows affected")

# NOTE USING THE PLACEHOLDER
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)


# SECTION _______ LIMIT HOW MANY RESULTS 

# sql = """
# SELECT *
# FROM
# customers
# LIMIT 5
# """
# mc.execute(sql)
# res=mc.fetchall()
# for x in res:
#     print(x)

# NOTE TO OFFSET WHERE YOU WANT TO START with (OFFSET)
sql = """
SELECT *
FROM
customers
LIMIT 5 OFFSET 2
"""
mc.execute(sql)
res = mc.fetchall()
for x in res:
    print(x)
