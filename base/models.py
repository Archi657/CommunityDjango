from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) 
    description = models.TextField(null=True, blank=True) # no description db/and form
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    updated = models.DateField(auto_now=True) # save it every time
    created = models.DateTimeField(auto_now_add=True) # snapshot once
    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateField(auto_now=True) # save it every time
    created = models.DateTimeField(auto_now_add=True) # snapshot once

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.body[0:15]
    