import psycopg2

def create_table():
   # 1 >>> Make a connection
    conn = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'post123' host = '127.0.0.1' port = '5432' ")

    # 2 >>> Make a cursor
    cur = conn.cursor()

    # 3 >>> Talk to Database
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #cur.execute("INSERT INTO store VALUES ('Wine Glass, 8, 10.5')")

    # 4 >>> Commit Changes
    conn.commit()

    # 5 >>> Close the connection 
    conn.close()

create_table()


def insert(item,quantity,price):
  
  conn = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'post123' host = '127.0.0.1' port = '5432' ")
  cur = conn.cursor()

  cur.execute(f"INSERT INTO store VALUES (%s, %s, %s)",(item,quantity,price))

  conn.commit()
  conn.close()


def view():
  conn = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'post123' host = '127.0.0.1' port = '5432' ")
  cur = conn.cursor()
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()
  conn.close()
  return rows

def delete(item):
  conn = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'post123' host = '127.0.0.1' port = '5432' ")
  cur = conn.cursor()
  cur.execute("DELETE FROM store WHERE item=%s",(item,))
  conn.commit()
  conn.close()



def update(item,quantity,price):
    conn = psycopg2.connect("dbname= 'database1' user = 'postgres' password = 'post123' host = '127.0.0.1' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()


update(item='Coffee Cup', quantity=10, price=30)
#delete('Apple')
print(view())

#insert('Apple', 2, 15)
















'''
import mysql.connector 

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"    
)

cursor = con.cursor()

word  = input("Search for word: ")

query = cursor.execute("SELECT  * FROM Dictionary WHERE Expression  = '{}' ".format(word))

results = cursor.fetchall()


if results:
  for ex in results:
    print(ex[0],'>>>' ,ex[1])
else:
    print('>>> {} <<< Not Found '.format(word))
'''