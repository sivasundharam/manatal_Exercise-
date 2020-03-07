from django.db import models
import os,binascii
# Create your models here.


class School(models.Model):

    name = models.CharField(max_length=20)
    no_students = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = "school"
        

def generateUUID():
    ''' generate random ascii string of length 20'''
    return binascii.b2a_hex(os.urandom(5)).decode("utf-8")

class Student(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_identification = models.CharField(max_length=20,unique=True, default=generateUUID)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "student"

    def clean(self):
       
        no_students = self.student.objects.count()
        allowed_students = School.objects.get(name=self.school)
        if no_students > allowed_students:
                raise ValidationError({"Error":_('School has reached max of students')})


