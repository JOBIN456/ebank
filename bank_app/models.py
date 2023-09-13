from django.db import models


class user(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    ACCOUNT_TYPE_CHOICES = [
        ('S', 'Savings Account'),
        ('C', 'Current Account'),
        ('F', 'Fixed Deposit Account'),
    ]

    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    branch = models.CharField(max_length=50)
    sub_branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    debit_card = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    cheque_book = models.BooleanField(default=False)
    def __str__(self):
        return self.name


