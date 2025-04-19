from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=221)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=221)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField(max_length=221)
    content = RichTextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Auhtor(models.Model):
    name = models.CharField(max_length=221)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    

class Comment(models.Model):
    name = models.CharField(max_length=221)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    if Article.objects.filter(slug=slugify(instance.title)).exclude(id=instance.id).exists():
        import uuid
        instance.slug += f"-{str(uuid.uuid4()).split('-')[0]}"

pre_save.connect(article_pre_save, sender=Article)
