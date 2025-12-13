from django.db import models
from accounts.models import User
from courses.models import Task


class Submission(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_ACCEPTED = 'Accepted'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_REJECTED, 'Rejected'),
    )

    user = models.ForeignKey(
        User,
        related_name='submissions',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='submissions',
        on_delete=models.CASCADE
    )
    answer = models.TextField()
    score = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} — {self.task.title}"
