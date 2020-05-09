from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #CASCADE -> user가 deleted되면 profile도 delete 하라
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    disability_types = (
        ('PD', '지체 장애'),
        ('VD', '시각 장애'),
        ('AD', '청각 장애'),
        ('W/B', '영유아 동반'),
    )
    disability = MultiSelectField(null=True, choices = disability_types)

    def __str__(self):
        return f'{self.user.username} 님의 프로필'

    def save(self):
        super().save()

        img = Image.open(self.image.path) # current instance의 image open

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)