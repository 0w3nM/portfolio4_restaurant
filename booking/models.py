from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


TIMES_AVAILABLE = [
    ('time1', "17:00"),
    ('time2', "17:15"),
    ('time3', "17:30"),
    ('time4', "17:45"),
    ('time5', "18:00"),
    ('time6', "18:15"),
    ('time7', "18:30"),
    ('time8', "18:45"),
    ('time9', "19:00"),
    ('time10', "19:15"),
    ('time11', "19:30"),
    ('time12', "19:45"),
    ('time13', "20:00"),
    ('time14', "20:15"),
    ('time15', "20:30"),
    ('time16', "20:45"),
]

PARTY_SIZE = [
    ('p_num1', '1'),
    ('p_num2', '2'),
    ('p_num3', '3'),
    ('p_num4', '4'),
    ('p_num5', '5'),
    ('p_num6', '6'),
    ('p_num7', '7'),
    ('p_num8', '8'),
    ('p_num9', '9'),
    ('p_num10', '10'),
]


class Reservation(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    day = models.DateField()
    time = models.CharField(choices=TIMES_AVAILABLE, max_length=10)
    party_size = models.CharField(choices=PARTY_SIZE, max_length=10)

    def __str__(self):
        return self.name
