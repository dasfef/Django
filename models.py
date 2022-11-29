from django.db import models

# Create your models here.
class Ff(models.Model) :
    f1 = models.IntegerField()
    f2 = models.CharField(max_length = 50)
    f3 = models.CharField(max_length = 50)

    def __str__(self) :
        return self.f3