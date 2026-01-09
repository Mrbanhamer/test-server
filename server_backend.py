import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'app_user',
    password = 'password123',
    database = 'mydatabase'
)

def connection():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'app_user',
        password = 'password123',
        database = 'mydatabase'
    )
    return mydb


def make_database():
    mydb = connection()
    mycursor = mydb.cursor()
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS namn (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
    """
    )
    mydb.commit()
    mycursor.close()
    mydb.close()

def add_new_data(name):
    mydb = connection()
    mycursor = mydb.cursor()
    mycursor.execute(
        'INSERT INTO namn (name) values (%s)',
        (name,)
    )
    mydb.commit()
    mycursor.close()
    mydb.close()

def show_data():
    mydb = connection()
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM namn')
    rows = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close
    return rows

#mycursor.execute('SELECT * FROM namn')
#rows = mycursor.fetchall()
#print(rows)

if __name__ == '__main__':
    make_database()
