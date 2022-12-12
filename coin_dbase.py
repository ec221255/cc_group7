# install dependencies
import os
import json
import sys
import pymysql

# Function return a connection.
db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn

def insert_currency(id, symbol, type, rateUsd):
    connection = open_connection()
    cursor = connection.cursor()
    query = "INSERT INTO `coincap` (`id`,`symbol`, `type`, `rateUsd`) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id, symbol, type, rateUsd))
    connection.commit()
    connection.close()
    
def select_currency(id):
    connection = open_connection()
    cursor = connection.cursor()
    query = "SELECT `id`,`symbol`, `type`, `rateUsd` FROM coincap WHERE id like %s"
    cursor.execute(query, (id))
    records = cursor.fetchall()
    print(records)
    connection.close()
    if not records:
        return 'No record found', ''
    else:
        return records[0][1], records[0][2], records[0][3], records[0][4]

if __name__ == '__main__':
    insert_currency(id='british-pound-sterling', symbol = "GBP", type = 'fiat', rateUsd = 1.2274035015367090)
    id, symbol, type, rateUsd = select_currency('british-pound-sterling')
    print(id, symbol, type, rateUsd)

'''
# Second Part

# connect to connection pool
with pool.connect() as db_conn:
  # create ratings table in our movies database
  db_conn.execute(
      "CREATE TABLE IF NOT EXISTS ratings "
      "( id SERIAL NOT NULL, title VARCHAR(255) NOT NULL, "
      "genre VARCHAR(255) NOT NULL, rating FLOAT NOT NULL, "
      "PRIMARY KEY (id));"
  )
  # insert data into our ratings table
  insert_stmt = sqlalchemy.text(
      "INSERT INTO ratings (title, genre, rating) VALUES (:title, :genre, :rating)",
  )
 
  # insert entries into table
  db_conn.execute(insert_stmt, title="Batman Begins", genre="Action", rating=8.5)
  db_conn.execute(insert_stmt, title="Star Wars: Return of the Jedi", genre="Action", rating=9.1)
  db_conn.execute(insert_stmt, title="The Breakfast Club", genre="Drama", rating=8.3)
 
  # query and fetch ratings table
  results = db_conn.execute("SELECT * FROM ratings").fetchall()
 
  # show results
  for row in results:
    print(row)'''
'''
def insert_data(city, lat, lng):
    connection = getConnection()
    cursor = connection.cursor()
    query = "INSERT INTO `city` (`city`, `lat`, `lng`) VALUES (%s, %s, %s)"
    cursor.execute(query, (city, lat, lng))
    connection.commit()
    connection.close()


def insert_uv_index(uv, uv_max, uv_max_time, uv_time):
    connection = getConnection()
    cursor = connection.cursor()
    query = "INSERT INTO `uv_index` (`uv`,`uv_max`,`uv_max_time`,`uv_time`) VALUES (%s, %s, %s, %s)"
    cursor.execute(query,(uv, uv_max, uv_max_time, uv_time))
    connection.commit()
    connection.close()

'''
'''
def delete_record(city):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT `city` FROM city WHERE `city`=%s"
    cursor.execute(query, (city))
    records = cursor.fetchall()
    if records:
        query = "DELETE FROM city where `city` like %s"  
        cursor.execute(query, (city))
        connection.commit()
        connection.close()
        return True
    else:
        connection.close()
        return False


def modify_record(city, lat, lng):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT `city` FROM city WHERE `city`=%s"
    cursor.execute(query, (city))
    records = cursor.fetchall()
    if records:
        query = "UPDATE city SET lat = %s, lng = %s WHERE `city` = %s"    
        cursor.execute(query, (lat, lng, city))
        connection.commit()
        connection.close()
        return f'Modified record for {city}'
    else:
        query = "INSERT INTO `city` (`city`, `lat`, `lng`) VALUES (%s, %s, %s)"    
        cursor.execute(query, (city, lat, lng))
        connection.commit()
        connection.close()
        return f'Created new record for {city}'

def insert_user(userName, password, role):
    
    connection = getConnection()
    cursor = connection.cursor()
    query = "INSERT INTO `users` (`Username`, `user_password`, `user_role`) VALUES (%s, %s, %s)"
    cursor.execute(query, (userName, password, role))
    connection.commit()
    connection.close()
    
       
def select_user(userName):
    connection = getConnection()
    cursor = connection.cursor()
    query = "SELECT Username, user_password, user_role FROM users WHERE Username like %s"
    cursor.execute(query, (userName))
    #records = cursor.fetchall() # (())
    account = cursor.fetchone()
    connection.close()
    return account


'''
# {"id":"british-pound-sterling","symbol":"GBP","currencySymbol":"£","type":"fiat","rateUsd":"1.2280290256940514"},
'''
if __name__ == '__main__':
    insert_data(id='british-pound-sterling', symbol = "GBP", currencySymbol = "£")
    symbol, currencySymbol = select_data('british-pound-sterling')
    print(symbol, currencySymbol)
modify_record(city='Paris', lat=48.864716, lng=2.349014)
    lat, lng = select_data('Paris')
    print(lat, lng)
    status = delete_record(city='Paris')
    print(status)
'''
