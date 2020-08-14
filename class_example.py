

class student:
    escuela = 'Telusko'


    @classmethod
    def info(cls):
        return cls.escuela

    @staticmethod
    def infor():
        print("This is student class")



print(student.info())

print(student.infor())
