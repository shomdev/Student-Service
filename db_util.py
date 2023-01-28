import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="23456",
  database="python_Student_db"
)
cursor=mydb.cursor()


def createCoursPriceTable():
    a = 'create table cours_price(BookID int(10) primary key, ItemName Varchar(20), Price float(10,2))' 
   
    cursor.execute(a)

def dropCoursPriceTable():
    b = 'drop table cours_price'
    cursor.execute(b)

def insertCoursPriceSingalData():
    b = 'insert into cours_price (BookID,ItemName,Price) values(%s,%s,%s)'
    c = (3,'php',399)

    cursor.execute(b,c)
    mydb.commit()

def insertCoursPriceManyData():
    d = 'insert into cours_price(BookID,ItemName,Price) values(%s,%s,%s)'
    e = [(4,'css',250),(5,'pytho',300),(6,'html',500)]

    cursor.executemany(d,e)
    mydb.commit()

def getCoursPriceData():
    f ='select * from cours_price'

    cursor.execute(f)
    x = []
 
    result = cursor.fetchall()

    for r in result:
        x.append(r)
    return x

def coursPriceUpdatTable():
    x = 'UPDATE cours_price SET Price=Price+100 WHERE Price<500'

    cursor.execute(x)
    mydb.commit()

def coursPriceDeleteRecord():
    h = "delete cours_price  where ItemName='python3'"

    cursor.execute(h)
    mydb.commit()
 