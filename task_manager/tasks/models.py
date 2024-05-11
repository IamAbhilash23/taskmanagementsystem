from django.db import models

class Tasks(models.Model):
    OPTION_ONE = 'To Do'
    OPTION_TWO = 'In Progress'
    OPTION_THREE = 'Done'

    CHOICES=[
        (OPTION_ONE, 'To Do'),
        (OPTION_TWO, 'In Progress'),
        (OPTION_THREE, 'Done'),
    ]
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    due_date=models.DateField(null=True)
    status=models.CharField(max_length=20,choices=CHOICES)
    def __str__(self):
        return self.title


