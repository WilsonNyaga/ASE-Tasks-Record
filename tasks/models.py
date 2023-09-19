from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add more fields as needed (e.g., address, phone number)

    def __str__(self):
        return self.name


class Task(models.Model):
    aircraft_registration = models.CharField(max_length=50)
    unit_description = models.TextField()
    unit_part_number = models.CharField(max_length=50)
    unit_serial_number = models.CharField(max_length=50)
    reported_snag = models.TextField()
    work_done = models.TextField()

    # Define a foreign key relationship to the Client model
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # Add additional fields or relationships as needed

    def __str__(self):
        return f"Task for {self.aircraft_registration}"


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on Task {self.task}"


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Attachment for Task {self.task}"
