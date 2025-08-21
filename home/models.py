from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Ensure this field exists
    message = models.TextField()  # Ensure this field exists

    def __str__(self):
        return self.email
