from django.db import models
# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=20,null=True,blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)
    DisplayFields=('id','first_name','last_name','dob','location')
    SearchableFields=['first_name','last_name']
    FilterFields=['location']


    class Meta:
        db_table="student"
