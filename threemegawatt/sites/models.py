from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " Site"


class Values(models.Model):
    site = models.ForeignKey(Site, related_name="values", on_delete=models.CASCADE)
    date = models.DateField()
    a_value = models.FloatField()
    b_value = models.FloatField()
