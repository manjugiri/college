from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    previouscollege = models.CharField(max_length=(20))
    email = models.EmailField()
    contact_no = models.CharField(max_length=10)
    program = models.CharField(max_length=10)

    def __self__(self):
        return self.name
