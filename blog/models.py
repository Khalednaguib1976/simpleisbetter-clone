from django.db import models


# Create your models here.
class post (models.Model):
    title =models.CharField(max_length=50)
    content =models.TextField(max_length=3000)
    veiwcont=models.IntegerField(default=0)
    image=models.ImageField(upload_to='posts/')




    def __str__(self):
        return self.title

    
    class Meta :
        ordering =('-id',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'

