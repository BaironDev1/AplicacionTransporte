from django.db import models

class Personal(models.Model):
    login_personal = models.CharField(max_length=50, unique=True) 
    clave_personal = models.CharField(max_length=50)  
    nombre_personal = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.nombre_personal} - {self.login_personal}"