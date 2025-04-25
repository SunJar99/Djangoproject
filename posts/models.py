from django.db import models
"""CREATE TABLE posts(id serial primary key autoincrement, title varchar(256), content varchar(856), rate int);"""

"""
all subjects SELECT * FROM post ==> Post.objects.all()
filtered objects SELECT * FROM post WHERE ILIKE('title) ==> Post.objects.filter(title__icontains='title')

one subject SELECT * FROM post WHERE id = 1 ==> Post.objects.get(id=1)
"""
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=256)

class Tag(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    title = models.CharField(max_length=356)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.title} {self.content} {self.id}"