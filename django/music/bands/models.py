from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    bands = models.ManyToManyField('Band', related_name='members')

    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # members field is automatically created due to the ManyToManyField in Member

    def __str__(self):
        return self.name