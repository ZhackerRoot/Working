from django.db import models
from django_countries.fields import CountryField

class Custom(models.Model):
     username = models.CharField(max_length=24)
     password = models.CharField(max_length=24)
     country = CountryField(null=False)
     class Meta:
        db_table = 'custom'

     def __str__(self):
        return self.username   

    #def get_absolute_url(self):
     #   return reverse('details', args=[str(self.pk)])
    