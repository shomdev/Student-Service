import db_util1 as dbutil

def createStudent():
 print('DO YOU WANT TO CREATE NEW STUDENT?')
 a = str(input('YES OR NO:   '))
 b = []


 if a == 'yes' or a == 'Yes' or a == 'YES':
    studentid = int(input('ID:   '))
    studentCount = dbutil.getStudetCount(studentid)
    if studentCount != 1:
        b.append(studentid)
        b.append(str(input('NAME:  ')))
        age = int(input('AGE:  '))
        allSubjects = str(input('SUBJECT:  '))
        i = allSubjects.replace(',',':')
        subjectCount = len(allSubjects.split(','))
        if age >= 20 and subjectCount >= 2:
            b.append(age)
            b.append(i)
            b.append(str(input('ADDRESS:  ')))
            print()
            print()
            x = tuple(b)
            dbutil.inseartInToStudentDb(x)
            print('USR HAS BEEN Successfull CREATED')
        else:print('try agen')
    else:print('uer already exist')
 else:print('Retry')

def studentFetchId():

 print('DO YOU WANT TO READ NEW STUDENT?')
 a = str(input('YES OR NO:   '))
 b = []
 if a == 'yes' or a == 'Yes' or a == 'YES':
    studentid = int(input('ID:   '))
    Sudentidlist = dbutil.fineIdStudentDb(studentid)
    x = len(Sudentidlist)
    if x == 1:
        print('Id:',Sudentidlist[0][0],)
        print('Name:', Sudentidlist[0][1])
        print('Age:', Sudentidlist[0][2])
        print('Subject:', Sudentidlist[0][3])
        print('Address:', Sudentidlist[0][4])

    else:print('this user not exist')
 else:print('retry')
 
def updateStudentRecord():
    pass


