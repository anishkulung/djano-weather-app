from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length = 25)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'
class City_cord(models.Model):
	lon = models.FloatField(null=True,blank=True)
	lat = models.FloatField(null=True,blank=True)
	city = models.ForeignKey('City',on_delete= models.CASCADE)
	def __str__(self):
		return "longitude:{},latitude:{}".format(self.lon,self.lat)