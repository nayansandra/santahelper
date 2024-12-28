
from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=[('Naughty', 'Naughty'), ('Nice', 'Nice')])

    def __str__(self):
        return self.name

class BehaviorData(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child.name} - {self.date_submitted}"
