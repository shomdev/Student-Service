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
        else:print('try again')
    else:print('uer already exist')
 else:print('Retry')

def studentFetchId():

 print('DO YOU WANT TO READ NEW STUDENT?')
 a = str(input('YES OR NO:   '))

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
    print('Do you want to update the student record?')
    a = str(input('YES OR NO:  '))
    b = []
   
    age = ['AGE', 'age', 'Age']
    subject  = ['SUBJECT', 'subject', 'Subject', 'Sub', 'sub']
    address = ['ADDRESS', 'address', 'Address', 'addr', 'Addr']
    
    if a == 'yes' or a == 'Yes' or a == 'YES':
        studentid = int(input('ID:   '))
        studentCount = dbutil.getStudetCount(studentid)
        if studentCount == 1:
            b.append(studentid)
            typeofdata = str(input('What do you want to change?(Age,Sub.,Addr.):  '))
            if typeofdata in age:
                b.append(str(input('Update Age:  ')))
                b.reverse()
                dbutil.udateStudentAge(b)
                print()
                print('Updated')
            if typeofdata in subject:
                allsubject = str(input('Update Subject: '))
                i = allsubject.replace(',',':')
                b.append(i)
                b.reverse()
                dbutil.udateStudentSubject(b)
                print()
                print('Updated')
            if typeofdata in address:
                b.append(str(input('Update Address:  ')))
                b.reverse()
                dbutil.udateStudentAddress(b)
                print()
                print('Updated')
        else:
            print('User not exist')
            print('Creat New Student')
    else:print('try again')


    
    

if __name__ == '__main__':
    updateStudentRecord()
