from django.db import models

# Create your models here.

class Record(models.Model):
    # saves when specific instance in that table/db was created
    create_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #email = models.EmailField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
