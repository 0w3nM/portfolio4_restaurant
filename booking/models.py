from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


TIMES_AVAILABLE = (
    ("17:00", "17:15"),
    ("17:30", "17:45"),
    ("18:00", "18:15"),
    ("18:30", "18:45"),
    ("19:00", "19:15"),
    ("19:30", "19:45"),
    ("20:00", "20:15"),
    ("20:30", "20:45"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25)
    day = models.DateField()
    time = models.CharField(choices=TIMES_AVAILABLE, max_length=10)
    party_size = models.IntegerField(default=1)

    def __str__(self):
        return self.name
