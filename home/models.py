from django.db import models

# Create your models here.
#UserAdd
class User( models.Model ):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100, unique=True)
    Mobile = models.CharField(max_length=50,primary_key=True)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.FirstName

'''class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=120)
    desc = models.TextField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.name
'''
'''class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(_(max_length=100)ssss
    email = models.models.EmailField(max_length=254)
    mobile_no = models.models.CharField(max_length=10)

    def __str__(self):
        return self.first_name'''

    
