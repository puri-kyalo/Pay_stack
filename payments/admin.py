

# Register your models here.
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'amount', 'reference', 'status', 'created_at')
    search_fields = ('reference', 'email')