from django.db import models


# Model for the project
class TasksData(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=300, null=True)
    created_at = models.DateField('Created', auto_now_add=True)
    update_at = models.DateField(auto_now=True, null=True, blank=True)
    isCompleted = models.BooleanField(default=False)
    date_completed = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
