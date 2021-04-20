from django.db import models

# Create your models here.
class bac_image_store(models.Model):
    class Meta:
        verbose_name_plural = 'Bacteria Image Database'
    
    S_no = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.S_no)

    