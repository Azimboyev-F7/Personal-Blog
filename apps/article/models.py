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
 
class Author(models.Model):
    name = models.CharField(max_length=221)
    bio = models.TextField()
    image = models.ImageField(upload_to='authors/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=221)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=221)
    content = RichTextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.title
    
class Subarticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=221)
    header_content = RichTextField()
    image = models.ImageField(upload_to='articles/')
    footer_content = RichTextField()

    def __str__(self):
        return self.title
    


    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)  
    name = models.CharField(max_length=221)
    message = models.TextField()
    image = models.ImageField(upload_to='comments/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    @property
    def get_children(self):
        return Comment.objects.filter(top_comment_id=self.id)
    
def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id



def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    if Article.objects.filter(slug=slugify(instance.title)).exclude(id=instance.id).exists():
        import uuid
        instance.slug += f"-{str(uuid.uuid4()).split('-')[0]}"

pre_save.connect(article_pre_save, sender=Article)
pre_save.connect(comment_pre_save, sender=Comment)