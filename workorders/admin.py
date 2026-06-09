from django.contrib import admin
from .models import WorkOrder

@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin):


    list_display = (
        'work_order_number',
        'title',
        'asset',
        'assigned_to',
        'status',
        'due_date',
        'created_date',
        'updated_date',
    )

    list_filter = (
        'status',
        'assigned_to',
    )

    search_fields = (
        'work_order_number',
        'title',
    )