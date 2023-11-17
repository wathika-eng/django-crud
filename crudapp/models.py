from django.db import models


# Create your models here.


class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    # profile_pic = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.first_name}+ " " +{self.last_name}'
