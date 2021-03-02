class Class_sg():
    LIST_OF_SUBJECTS = [ 'Art', 'Biology', 'Geography',
                         'History', 'Literature', 'Math' ,'Physical education', 'Physics']
    
    def __init__(self,nbOfClass):
        self.__nbOfClass = nbOfClass
        self.teacherById = list()
        self.studentsById = set()
        self.examDates= dict()
        
    @property
    def nbOfClass(self):
        return self.__nbOfClass
    
    @classmethod
    def addNewSubjectToAllClasses(cls,subjectToAdd):
        cls.LIST_OF_SUBJECTS.append(subjectToAdd)
        return cls
    
    @classmethod
    def removeSubjectorFromAllClasses(cls,subjectToRemove):
        cls.LIST_OF_SUBJECTS.remove(subjectToRemove)
        return cls
    
    @staticmethod
    def isClassNumberIsPair(nbOfClass):
        if (nbOfClass % 2) == 0:
           return True
        else:
           return False

    def removeSubjectorFromAllClasses(self, teacherByIdToAdd):
        self.teacherById.append(teacherByIdToAdd)
    
    def addTeacher(self, teacherByIdToAdd):
        self.teacherById.append(teacherByIdToAdd)
    
    
    def removeTeacher(self, teacherByIdToRemove):
        self.teacherById.remove(teacherByIdToRemove)
    
    def get_AllTeacherById(self):
        return self.teacherById
    
    def addStudent(self, studentIDToAdd):
        try:
            self.studentsById.update(studentIDToAdd)
        except:
            self.studentsById.add(studentIDToAdd)
    
    def removeStudent(self, studentByIdToRemove):
        self.studentsById.remove(studentByIdToRemove)
            
    def get_AllStudentsById(self):
        return self.studentsById      
            
    def setNextExamDate(self,subject,date):
        if (subject not in self.LIST_OF_SUBJECTS):
            return print('No such subject as {0}, cannot set an exam'.format(subject))
        else:
            self.examDates[subject]=date
        
    def removeExamDate(self,subject):
        self.examDates.pop(subject)

    def getExamDate(self, subject):
        try:
            return self.examDates[subject]
        except:
            return print("No date is set for {0}".format(subject))
        
    def getAllExamDates(self):
        return self.examDates
        
