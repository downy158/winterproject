from django.db import models
from django.utils import timezone


class Space(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    SPACE_TYPE_CHOICES = (
        ('THEATER','소극장'),
        ('METTINGROOM', '회의실'),
        ('PARKING', '주차장'),
    )
    space_type = models.CharField(max_length=10, choices=SPACE_TYPE_CHOICES, default ='THEATER')
    address1 = models.CharField(max_length=10)
    address2 = models.CharField(max_length=10)
    address3 = models.CharField(max_length=10)
    description = models.TextField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @classmethod
    def space_type_to_korean(cls, space_type):
        for choice in cls.SPACE_TYPE_CHOICES:
            if choice[0] == space_type:
                return choice[1]

        return None

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
