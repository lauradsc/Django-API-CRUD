from django.db import models

# Create your models here.

class User(models.Model):
    
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self): #NOTE - uma método que retornará um resultado em string, não necessitanto ser chamada para ser ativada
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
