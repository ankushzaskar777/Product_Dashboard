from django.db import models

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    price = models.IntegerField()
    pimage = models.ImageField(upload_to='image/', null=True, blank=True)
    description = models.CharField(max_length=101)

    def __str__(self):
        return self.pname
