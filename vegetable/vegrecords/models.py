from django.db import models

# Create your models here.
class Veg(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    price=models.IntegerField()


class Farmer(models.Model):
    veg=models.ForeignKey(Veg,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    fid=models.IntegerField()


    class Meta:
        db_table='Farm'
