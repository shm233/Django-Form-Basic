from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='media/student', null=True)
    address = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.name}"
    