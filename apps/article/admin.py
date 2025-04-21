from django.contrib import admin
from .models import Article, Category, Comment, Tags, Author, Subarticle
# Register your models here.

class SubarticleInline(admin.StackedInline):  # yoki admin.StackedInline
    model = Subarticle
    extra = 1  # Qo'shimcha bo'sh formalar soni

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubarticleInline,)
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-id',)
    date_hierarchy = 'created_at'
    readonly_fields = ('slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-id',)
    date_hierarchy = 'created_at'

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-id',)
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
