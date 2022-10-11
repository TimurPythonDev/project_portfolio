from unicodedata import name
from django.db import models





class HomeViewModel(models.Model):

    name_title = models.CharField(max_length=120)
    

    def __str__(self):
        return self.name_title


    class Meta:
        verbose_name = "Home Name"
        verbose_name_plural = "Home Names"
        


class HomefieldModels(models.Model):

    field_name = models.FileField(upload_to='media/', max_length=254, null=True,blank=True)

    class Meta:
        verbose_name = "Home Resume"
        verbose_name_plural = "Home Resumes"

 