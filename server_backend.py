import mysql.connector

namn = 'variables'

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'app_user',
    password = 'password123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

def make_database():
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS namn (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )             
    """
    )

def add_new_data(name):
    mycursor.execute(
        'INSERT INTO namn (name) values (%s)',
        (namn,)
    )
    mydb.commit()

#mycursor.execute('SELECT * FROM namn')
#rows = mycursor.fetchall()
#print(rows)

if __name__ == '__main__':
    make_database()

mycursor.close()
mydb.close()
