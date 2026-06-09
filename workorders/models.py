from django.db import models
from assets.models import Asset
from django.contrib.auth.models import User

class WorkOrder(models.Model):

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    work_order_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    created_date = models.DateField(
        auto_now_add=True
    )
    
    updated_date = models.DateTimeField(
        auto_now=True
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_work_orders'
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )    

    def __str__(self):
        return f"{self.work_order_number} - {self.title}"
