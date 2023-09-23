from django.db import models

# Create your models here.


class StudentModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        StudentModel, on_delete=models.CASCADE, related_name='course')
    name = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self) -> str:
        # return f'{self.name}- marks: {self.marks}'
        return self.name
