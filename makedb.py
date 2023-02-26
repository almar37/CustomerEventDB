import sqlite3
import pandas as pd 

conn = sqlite3.connect('db.sqlite3') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS customer_customer
          ([id] INTEGER PRIMARY KEY, [customer_name] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS customer_event
          ([id] INTEGER PRIMARY KEY, [event] TEXT)
          ''')
                     
conn.commit()

c.execute('''
          INSERT INTO customer_customer (id, customer_name)

                VALUES
                (1,'Lenin'),
                (2,'Gaddafi'),
                (3,'Stalin'),
                (4,'Hitler'),
                (5,'Saddam')
          ''')

c.execute('''
          INSERT INTO customer_event (id, event)

                VALUES
                (1,'SAFARI'),
                (2,'SCUBA'),
                (3,'SAFARI'),
                (4,'SAFARI'),
                (5,'SCUBA')
          ''')

conn.commit()

c.execute('''
          SELECT
          a.customer_name,
          b.event
          FROM customer_customer a
          LEFT JOIN customer_event b ON a.id = b.id
          ''')

df = pd.DataFrame(c.fetchall(), columns=['customer_name','event'])
print (df)