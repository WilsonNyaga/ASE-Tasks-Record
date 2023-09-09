from django.db import models

# Create your models here.
from django.db import models

class Aircraft(models.Model):
    registration = models.CharField(max_length=10)
    client = models.CharField(max_length=100)
    reported_snag = models.TextField()
    work_done = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    job_number = models.IntegerField()
    unit_description_name = models.CharField(max_length=100)
    unit_description_part_number = models.CharField(max_length=50)
    unit_description_serial_number = models.CharField(max_length=50)

    def __str__(self):
        return self.registration  # Display the aircraft registration as the object's string representation
