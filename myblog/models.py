from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

def image_path(instance, filename):
    #file name is the raw image name ex:fz54s8e.jpg
    ext = filename.split('.')[1]
    return f'{instance.slug}.{ext}'

class Blog(models.Model):
    title           = models.CharField(max_length=100, unique=True)
    slug            = models.SlugField(blank=True)
    content         = models.TextField()
    publish_date    = models.DateTimeField(auto_now_add=True)
    thumbnail       = models.ImageField(upload_to=image_path)
    number_of_reads = models.IntegerField(default=0)
    author          = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:30]+"..."

    objects = models.Manager()

class Comment(models.Model):
    blog             = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    text             = models.TextField(blank=True, null=True)
    date             = models.DateField(auto_now=True)
    parent_comment   = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    
    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()

    objects = models.Manager()

@receiver(pre_save, sender=Blog)
def slug_generator(sender, instance, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug
    