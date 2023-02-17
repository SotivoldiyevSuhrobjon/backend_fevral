from django.db import models
from django.contrib.auth.models import User         


class Todo(models.Model):
    sifat_type=(
        ('Alo','Alo'),('yaxshi','yaxshi'),('orta','orta')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    narx = models.CharField(max_length=15)
    sifat = models.CharField(max_length=50, choices=sifat_type)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user} - {self.title}"


