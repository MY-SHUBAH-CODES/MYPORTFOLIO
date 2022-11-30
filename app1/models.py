from django.db import models

class MyCirtificates(models.Model):
    mycv=models.FileField(upload_to='mycv')
    

