import psycopg2
from api import RequestManager

connection = psycopg2.connect(
    database='json_19_30',
    user='postgres',
    password='123456',
    host='localhost'
)

cursor = connection.cursor()

cursor.execute('''
    drop table if exists CATEGORIES;
    create table if not exists CATEGORIES(
        category_id integer primary key generated always as identity,
        category_name varchar(50)        
    );
    drop table if exists 
''')

connection.commit()
# connection.close()

request_manager = RequestManager()
categories = request_manager.get('/products/categories/')

for category in categories:
    cursor.execute('insert into CATEGORIES(category_name) values(%s)', (category,))

connection.commit()
connection.close()
