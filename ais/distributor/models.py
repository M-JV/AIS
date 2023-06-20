from django.db import models

# Create your models here.
class Distributor(models.Model):
    distributorName = models.CharField(max_length=20)
    distributorEmail = models.EmailField(max_length=50)
    distributorContact = models.CharField(max_length=11)
    distributorPassword = models.CharField(max_length=20)
    distributorToken = models.CharField(max_length=4,default='0000')
    

    class Meta:
        db_table = 'Distributor Info'


class TemporaryD(models.Model):
    distributorName = models.CharField(max_length=20)
    distributorPassword = models.CharField(max_length=20)

    class Meta:
        db_table = 'Distributor Temporary Data'