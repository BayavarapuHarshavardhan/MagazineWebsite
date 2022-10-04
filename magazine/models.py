from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Magazine(models.Model):
    title = models.CharField(max_length=50,default="Article")
    desc = models.TextField(default="Its time to read more about the Article")
    img = models.ImageField(upload_to='pics',default='pics/article.jpg')
    email=models.EmailField(default="abcd@gmail.com")
    def __str__(self):
     return "{0}->{1}".format(self.title, self.email)