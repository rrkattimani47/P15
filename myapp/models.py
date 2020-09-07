from django.db import models
# Create your models here.

class topic(models.Model):
    topic_name=models.CharField(max_length=30,unique=True,blank=False)

    def __str__(self):
        return self.topic_name
class webpage(models.Model):
    topic=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True,blank=False)
    url=models.URLField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.name
class accessDetails(models.Model):
    webpage=models.ForeignKey(webpage,on_delete=models.CASCADE)
    datetime=models.DateTimeField()

    def __str__(self):
        return str(self.datetime).split(" ")[0]
