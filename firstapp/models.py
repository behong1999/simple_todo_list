from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    #NOTE: Rememebr to makemigrations and migrate to update the database
    user = models.ForeignKey(User,on_delete=models.CASCADE
                            # ,related_name="todolist"
                            )
    name = models.CharField(max_length=200)
    
    # Represent the class objects as a string - it can be used for classes.
    def __str__(self):
        return self.name


class Item(models.Model):
    # When the referenced object is deleted, 
    # also delete the objects that have references to it 
    # (when you remove a blog post for instance, 
    #  you might want to delete comments as well)
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    txt = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def  __str__(self):
        return self.txt
        