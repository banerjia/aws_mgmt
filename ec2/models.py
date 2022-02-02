from django.db import models
# Create your models here.
class Instance(models.Model):

    instance_id = models.CharField(primary_key=True, max_length=64, editable=False)
    instance_name = models.CharField(max_length=255)
    instance_state = models.CharField(max_length=64, editable=False)
    instance_new_state = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.instance_name
