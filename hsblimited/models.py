from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(max_length=254,primary_key=True)
    fullname=models.CharField(max_length=254)
    mobile=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    password=models.CharField(max_length=50)


class LoanApplication(models.Model):
    loan_id=models.BigAutoField(primary_key=True)
    user_email=models.ForeignKey(User,on_delete=models.CASCADE)
    loan_type=models.CharField(max_length=100)
    loan_amount=models.IntegerField(default=0)
    address=models.CharField(max_length=254)
    approved_amount=models.IntegerField(default=0)
    status=models.CharField(default="Applied",max_length=30)


