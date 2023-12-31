from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def get_absolute_url(self):
        return reverse("notes", args=[str(self.id)])
    
class Vault(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("Note:Vault-Url", args=[str(self.id)])
    def __str__(self):
        return f'{self.name} - {self.user.username}'
    
class Note(models.Model):
    title = models.CharField(max_length=40)
    Tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    Deleted = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse("Note:Note-Url", args=[str(self.id)])
    def __str__(self):
        return self.title
class Pragraph(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name  = "pragraph")
    Text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("Note:Pragraph-Url", args=[str(self.id)])
    def __str__(self):
        return f'{self.Text} - created at : {self.created}'
    class Meta:
        ordering = ["created"]
    
class Link(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name = "link")
    url = models.CharField(max_length=300)

