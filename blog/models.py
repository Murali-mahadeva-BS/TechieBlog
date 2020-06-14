from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


class Post(models.Model):
    id = models.UUIDField(  # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    dateposted = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=30)
    # author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title_img = models.ImageField(
        default='default.png', upload_to='title_images')
    content = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
