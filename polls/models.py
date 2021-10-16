from django.db import models

class Convert(models.Model):
    
    
    slug = models.SlugField(("Silka "), max_length=100)
    image = models.ImageField()

    class Meta:
        verbose_name = ("Convert")
        verbose_name_plural = ("Converts")

    def __str__(self):
        return f'{self.id}'


