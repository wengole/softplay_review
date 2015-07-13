from django.db import models


class SoftPlayCentre(models.Model):
    title = models.TextField()
    address = models.TextField()
    hours = models.ForeignKey('Hours')
    fees = models.TextField()
    facilities = models.TextField()
    parking = models.BooleanField()

    def rating(self):
        pass


class Hours(models.Model):
    pass


class Fees():
    pass


class Review(models.Model):
    pass
