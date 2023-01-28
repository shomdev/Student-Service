import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="23456",
  database="student_db1"
)
cursor=mydb.cursor()



def inseartInToStudentDb(inputTuple):
    c = 'insert into student_db1 (ID,NAME,AGE,SUBJECT,ADDRESS) values(%s,%s,%s,%s,%s)'
    cursor.execute(c,inputTuple)
    mydb.commit() 

def getStudetCount(Id):
    cursor.execute('Select Count(*) From student_db1 Where ID = ' + str(Id))

    myresult = cursor.fetchone()

    return(myresult[0])

def fineIdStudentDb(Id):
  a = ("select * from student_db1 where ID = " + str(Id))
  cursor.execute(a)
  b = cursor.fetchall()
  return(b)


if __name__ == '__main__':
 C = fineIdStudentDb(12)
 print(C)
