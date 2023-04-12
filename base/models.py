import os
import random
from django.db import models
from accounts.models import User


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 2541781232)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "img/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class Genre(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Tier(models.Model):
    TIER_CHOICES = (
        ('1', 'Tier 1'),
        ('2', 'Tier 2'),
        ('3', 'Tier 3'),
    )

    PLAN_IDS = {
        '1': 'P-8U773388PW8654051MQQ5TNQ',
        '2': 'P-00529703HN3318227MQQ5VSI',
        '3': 'P-28D816824R709661FMQQ5WMQ',
    }
    
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, unique=True)
    plan_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Tier {self.tier}'

    def save(self, *args, **kwargs):
        self.plan_id = self.PLAN_IDS[self.tier]
        super().save(*args, **kwargs)


class Product(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True, related_name='genre')
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text