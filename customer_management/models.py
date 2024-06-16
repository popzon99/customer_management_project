from bson import ObjectId
from django.db import models
from django.contrib.auth.models import AbstractUser

class ObjectIdField(models.Field):
    def get_internal_type(self):
        return "ObjectIdField"

    def to_python(self, value):
        if isinstance(value, ObjectId):
            return value
        elif value is None:
            return value
        return ObjectId(value)

    def get_prep_value(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        elif value is None:
            return value
        return str(ObjectId(value))

class User(AbstractUser):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    ROLE_CHOICES = (
        ('maker', 'Maker'),
        ('checker', 'Checker'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    assigned_checker = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='makers')

    def __str__(self):
        return self.username

class Customer(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='customer_photos/')
    resume = models.FileField(upload_to='customer_resumes/')
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')

    def __str__(self):
        return self.name

class CustomerStatus(models.Model):
    id = ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    )
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='status')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    checker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='statuses')

    def __str__(self):
        return f"{self.customer.name} - {self.status}"
