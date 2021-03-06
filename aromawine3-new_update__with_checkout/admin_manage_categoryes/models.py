from django.db import models
from datetime import date
from django.contrib.auth.models import User
import django
# Create your models here.

def user_directory_path(instance, filename):
    producer_id_in_list = instance.Category_name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/categoryes/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)

class AwCategory(models.Model):
    Category_name  = models.CharField(max_length=120,unique=True)
    Title = models.CharField(max_length=500)
    Image = models.ImageField(upload_to=user_directory_path)
    Description = models.TextField(null=True,blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Created_by_AwCategoryes')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Updated_by_AwCategoryes')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Category_name)
    class Meta:
        verbose_name_plural = "AW Categoryes"