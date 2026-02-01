from django.db import models

class Partner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='partner/')
    url = models.URLField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f'{self.first_name} {self.last_name} - {self.position} at {self.company}'
    
class Feature(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
