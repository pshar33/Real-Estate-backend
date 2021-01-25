from django.db import models

# Create your models here.
class Person(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contacted = models.CharField(max_length=200)
    notes = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


    def __str__(self):

        return '%s by %s' % (self.first_name, self.last_name)