from django.db import models



class Book(models.Model):
    CATEGORY_CHOICES = (
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography'),
        ('science', 'Science'),
        ('fantasy', 'Fantasy'),
    )
    
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
































# Create your models here.
class Patient(models.Model):
    CATEGORY_CHOICES = (
        ('burn', 'Burn'),
        ('emergency', 'Emergency'),
        ('regular', 'Regular'),
    )
    name = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    age = models.IntegerField()
    date_of_visit = models.DateField()
    follow_up_status = models.BooleanField(default=False)
    examination_or_operation_fees = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
