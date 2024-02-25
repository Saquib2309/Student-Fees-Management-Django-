from django.db import models

# Create your models here.
class admindata(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email

class operatordata(models.Model):
    name=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.email

class studentdata(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email

class logindata(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class photodata(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    photo=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class course_master(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=100)
    fees=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class st_course(models.Model):
    st_course_id=models.AutoField(primary_key=True)
    course_id=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    course_name=models.CharField(max_length=100)
    fees=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    commencement_date=models.DateField()


    def __str__(self):
        return self.email

class st_installment(models.Model):
    t_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    course_id=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    t_date=models.DateField()
    remark=models.CharField(max_length=100)

    def __str__(self):
        return self.email
