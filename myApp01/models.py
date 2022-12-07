from django.db import models

# Create your models here.
class Essay (models.Model) :
    sTitle = models.CharField(max_length = 50)
    sText = models.TextField()
    dateTime = models.DateTimeField()
    
    def publish(self) :
        self.dateTime = timezone.Now()
        self.save()
    
    def __str__(self) :
        return self.sTitle
