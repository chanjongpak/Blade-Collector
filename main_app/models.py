from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
DUTIES = (
    ('S', 'Sharpen Blade'),
    ('O', 'Oil & Wipe Blade'),
    ('D', 'Dust Sheath')
)

class Accessory(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})

class Blade(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    weight = models.IntegerField()
    flexibility = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'blade_id': self.id})


class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    duty = models.CharField(max_length=1,
    choices=DUTIES, default=DUTIES[0][0])

    blade = models.ForeignKey(Blade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_duty_display()} on {self.date}"

    class Meta:
        ordering = ['-date']