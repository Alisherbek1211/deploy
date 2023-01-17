from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    task = models.TextField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.task