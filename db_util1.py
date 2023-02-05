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

def udateStudentAge(inputTuple):
  a = ('UPDATE student_db1 SET AGE = %s  WHERE ID = %s')

  cursor.execute(a,inputTuple)
  mydb.commit()

def udateStudentAddress(inputTuple):
  a = ('UPDATE student_db1 SET ADDRESS = %s  WHERE ID = %s')

  cursor.execute(a,inputTuple)
  mydb.commit()

def udateStudentSubject(inputTuple):
  a = ('UPDATE student_db1 SET SUBJECT = %s  WHERE ID = %s')

  cursor.execute(a,inputTuple)
  mydb.commit()

def deleteStudenRecord(ID):
  a = ('DELETE FROM student_db1 WHERE ID = ' +str(ID))

  cursor.execute(a)
  mydb.commit()

if __name__ == '__main__':
  deleteStudenRecord(8)

