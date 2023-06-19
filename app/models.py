from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=90)
    LOC=models.CharField(max_length=90)
class EMP(models.Model):
    EMPNO=models.IntegerField()
    ENAME=models.CharField(max_length=80)
    JOB=models.CharField(max_length=70)
    SAL=models.IntegerField()
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)