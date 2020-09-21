from datetime import datetime
now = datetime.now()


DOB = arr(input('what is your DOB? enter in dd,mm,yy format.'))


class Record:
     
     def __init__(self,forename,surname,age: int,gender,CS_student,DOB):
          
          #attributes
          if not isinstance(forename, str):
               raise TypeError('forename must be an string')
          else:
               self.__forename = forename

          if not isinstance(surname, str):
               raise TypeError('surname must be an string')
          else:
               self.__surname = surname
          
          if not isinstance(age, int):
               raise TypeError('age must be an integer')
          else:
               self.__age = age

          self.__gender = gender
          while self.__gender not in {'F', 'M' , 'O'}:
               raise TypeError('gender must be M, F or O')
          
          self.__CS_student = CS_student
          while self.__CS_student not in {'True', 'False'}:
               raise TypeError('must be True or False')

          self.__DOB = DOB

     #methods
     def get_DOB(self):
          return self.__gender
          
     def get_forename(self):
          return self.__forename

     def get_surname(self):
          return self.__surname

     def set_age(self,age):
          self.__age = age
          return self.__age

     def get_gender(self):
          return self.__gender

     def set_gender(self,gender):
          self.__gender = gender
          return self.__gender     

     def get_age(self):
          age = 2020 - DOB(2)
          return self.__age

     def set_age(self,age):
          self.__age = age
          return self.__age
          
     def get_CS_student(self):
          return self.__CS_student
     
     def set_CS_student(self,CS_student):
          self.__CS_student = CS_student
          return self.__CS_student
     
     def set_forename(self,forename):
          self.__forename = forename
          return self.__forename

     def set_surname(self,surname):
          self.__surname = surname
          return self.__surname
               

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")         
record1 = Record('Demira','Thaker',16, 'F','True','16,11,03')
print(record1.get_gender(), dt_string)
print(record1.get_age())
record1.set_forename('bob')

