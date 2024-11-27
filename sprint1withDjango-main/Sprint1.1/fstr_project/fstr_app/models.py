from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Coords(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    height = models.IntegerField()

class Pereval(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.TextField(blank=True)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField()
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level_winter = models.CharField(max_length=50, blank=True)
    level_summer = models.CharField(max_length=50, blank=True)
    level_autumn = models.CharField(max_length=50, blank=True)
    level_spring = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')

class PerevalImage(models.Model):
    pereval = models.ForeignKey(Pereval, related_name='images', on_delete=models.CASCADE)
    img = models.BinaryField()  # Или можете хранить ссылки на изображения
    title = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Pereval.STATUS_CHOICES, default='new')

